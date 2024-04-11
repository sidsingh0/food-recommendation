from flask import make_response
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
from flask import make_response, jsonify
import random
import ast

class dish_model():

    def __init__(self):
        with open('data/nearest_dishes_model.pkl', 'rb') as file:
            self.model = pickle.load(file)
        self.df=pd.read_csv('data/dishes.csv').dropna(subset=['description', 'ingredients', 'tags', 'name', 'calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates'])
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.description_vec = self.vectorizer.fit_transform(self.df['description'].astype(str))
        self.ingredients_vec = self.vectorizer.fit_transform(self.df['ingredients'].astype(str))
        self.tags_vec = self.vectorizer.fit_transform(self.df['tags'].astype(str))
        self.name_vec = self.vectorizer.fit_transform(self.df['name'].astype(str))
        self.scaler = StandardScaler()
        self.numerical_features = self.df[['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']]
        self.numerical_features_scaled = self.scaler.fit_transform(self.numerical_features)
        print("Model loaded successfully")

    def recommend_model(self,id):
        try:
            id=int(id)
            input_combined_features =  hstack([self.description_vec[id] * 0.1, self.tags_vec[id] * 0.1, self.name_vec[id] * 0.15, self.ingredients_vec[id] * 0.4, self.numerical_features_scaled[id].reshape(1, -1) * 0.35])
            nearest_dishes_distances, nearest_dishes_indices = self.model.kneighbors(input_combined_features)
            index_list=nearest_dishes_indices.flatten().tolist()
            recommended_details=[]
            for i in index_list:
                row_dict = self.df.loc[self.df.index == i].to_dict(orient='records')
                if row_dict:
                    recommended_details.append(row_dict[0])
            current_dish=self.df.iloc[id].to_dict()
            random.shuffle(recommended_details)
            return make_response({"dishes":recommended_details[:8],"currentdish":current_dish,"success":1},200)
        except (ValueError, IndexError) as e:
            return make_response({"message": "Invalid ID","success":0}, 200)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error.","success":0},200)

    def prompt_recommend_model(self,data):
        try:
            input_ingredients=data.get("ingredients")
            input_minutes=data.get("minutes")
        except KeyError:
            return make_response({"message": "Missing required fields in input","success":0}, 200)
        except Exception as e:
            return make_response({"message":"Invalid input","success":0},200)

        try:
            if (input_minutes==""):
                input_minutes=200000
            input_minutes=int(input_minutes)
            input_ingredients_set = set()
            for i in input_ingredients.split(','):
                input_ingredients_set.add(i.strip())
            if (len(input_ingredients_set)<1):
                return make_response({"message": "Invalid input","success":0}, 200)
        except:
            return make_response({"message": "Invalid input","success":0}, 200)
            
        try:
            matching_details = []
            for index, row in self.df.iterrows():
                row_ingredients_set = set([i.strip() for i in row['ingredients'].split(',')])
                if row_ingredients_set.issubset(input_ingredients_set) and row['minutes'] <= input_minutes:
                    matching_details.append(row.to_dict())
                    
            if len(matching_details) < 1:
                return {"message": "No items match your input.","success":0}, 200
            else:
                return {"dishes": matching_details,"success":1}, 200
        except Exception as e:
            print(e)
            return {"message": "Internal server error.","success":0}, 200   

    def recommend_list(self,wishlist):
        try:
            wishlist_length=len(wishlist)
        except:
            return make_response({"message": "No items in wishlist.","wishlist_count":0,"success":0}, 200)
        try:
            if (wishlist_length==0):
                return make_response({"message":"No items in wishlist.","wishlist_count":0,"success":0},200)
            if (wishlist_length>0):
                if (wishlist_length<3):
                    random_elements=wishlist
                else:
                    random_elements = random.sample(wishlist, 3)
                combined_recommendation_list=[]
                recommended_details=[]
                wishlist_details=[]
                for i in random_elements:
                    input_combined_features =  hstack([self.description_vec[i] * 0.1, self.tags_vec[i] * 0.1, self.name_vec[i] * 0.15, self.ingredients_vec[i] * 0.4, self.numerical_features_scaled[i].reshape(1, -1) * 0.35])
                    nearest_dishes_distances, nearest_dishes_indices = self.model.kneighbors(input_combined_features)
                    index_list=nearest_dishes_indices.flatten().tolist()[:8]
                    combined_recommendation_list.extend(index_list)
                random.shuffle(combined_recommendation_list)
                for i in wishlist:
                    row_dict = self.df.loc[self.df.index == i].to_dict(orient='records')
                    if row_dict:
                        wishlist_details.append(row_dict[0])
                for i in combined_recommendation_list:
                    row_dict = self.df.loc[self.df.index == i].to_dict(orient='records')
                    if row_dict:
                        recommended_details.append(row_dict[0])
                # final_response=json.dumps(})
                return make_response({"dishes":recommended_details[:8],"wishlist":wishlist_details,"success":1}),200
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error.","success":0},200)

    
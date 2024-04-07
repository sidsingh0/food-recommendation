import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
from flask import make_response
import random
import ast

class Recommender():
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

    def recommend(self,id):
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
            random.shuffle(recommended_details)
            return make_response({"dishes":recommended_details[:8]},200)
        except (ValueError, IndexError) as e:
            return make_response({"message": "Invalid ID"}, 400)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

    def recommend_list(self,wishlist):
        try:
            wishlist_length=len(wishlist)
        except:
            return make_response({"message": "No items in wishlist."}, 204)
        try:
            if (wishlist_length==0):
                return make_response({"message":"No items in wishlist."},204)
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
                return make_response({"dishes":recommended_details[:8],"wishlist":wishlist_details},200)    
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)
    
    def recommend_prompt(self,input_ingredients,input_minutes=200000):
        try:
            input_minutes=int(input_minutes)
            input_ingredients_set = set()
            for i in input_ingredients.split(','):
                input_ingredients_set.add(i.strip())
            if (len(input_ingredients_set)<1):
                return make_response({"message": "Invalid input"}, 400)
            if not input_minutes or input_ingredients:
                return make_response({"message": "Invalid input"}, 400)
        except:
            return make_response({"message": "Invalid input"}, 400)
        try:
            matching_details = []
            for index, row in self.df.iterrows():
                row_ingredients_set=ast.literal_eval(row['ingredients_set'])
                if row_ingredients_set.issubset(input_ingredients_set) and row['minutes'] <= input_minutes:
                    matching_details.append(row.to_dict())
                    
            if len(matching_details) < 1:
                return {"message": "No items match your input."}, 204
            else:
                return {"dishes": matching_details}, 200
        except Exception as e:
            print(e)
            return {"message": "Internal server error."}, 500
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
        # initialising all the dependencies needed to run recommendation models
        with open('data/nearest_dishes_model.pkl', 'rb') as file:
            self.model = pickle.load(file)
        self.df=pd.read_csv('data/dishes.csv')
        self.df['tags'] = self.df['tags'].fillna(' ')
        self.maxtime = int(self.df['minutes'].max())

        #vectorizing textual values
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.description_vec = self.vectorizer.fit_transform(self.df['description'])
        self.ingredients_vec = self.vectorizer.fit_transform(self.df['ingredients'])
        self.tags_vec = self.vectorizer.fit_transform(self.df['tags'])
        self.name_vec = self.vectorizer.fit_transform(self.df['name'])
        #scaling numerical values
        self.scaler = StandardScaler()
        self.numerical_features = self.df[['calories', 'total_fat', 'sugar', 'sodium', 'protein', 'saturated_fat', 'carbohydrates']]
        self.numerical_features_scaled = self.scaler.fit_transform(self.numerical_features)
        print("Recommendation Model loaded successfully")
        
        #loading the second model for search
        with open('data/nearest_ingredients_model.pkl', 'rb') as file:
            self.ingredient_model = pickle.load(file)
        self.ingredient_model_vectorizer = TfidfVectorizer(stop_words='english')
        self.ingredient_model_vec = self.ingredient_model_vectorizer.fit_transform(self.df['ingredients'])
        print("Search Model loaded successfully")
        
    # function to get dataset's rows based on a index or a list of indexes
    def indices_to_dict(self, row_index):
        if isinstance(row_index, int):
            return self.df.iloc[row_index].to_dict()
        if isinstance(row_index, list):
            recommended_details=[]
            for i in row_index:
                row_dict = self.df.loc[self.df.index == i].to_dict(orient='records')
                if row_dict:
                    recommended_details.append(row_dict[0])
            random.shuffle(recommended_details)
            return(recommended_details)

    def recommend_model(self,id):
        try:
            id=int(id)

            # using id to get all the vectorised and scaled values
            input_combined_features =  hstack([self.description_vec[id] * 0.1, self.tags_vec[id] * 0.1, self.name_vec[id] * 0.15, self.ingredients_vec[id] * 0.4, self.numerical_features_scaled[id].reshape(1, -1) * 0.35])
            
            # applying the model
            nearest_dishes_distances, nearest_dishes_indices = self.model.kneighbors(input_combined_features)
            index_list=nearest_dishes_indices.flatten().tolist()

            # removing the dish if it exists in recommended recipes
            if (id in index_list):
                index_list.remove(id)
                
            # replying with details of requested dish and recommendations
            recommended_details=self.indices_to_dict(index_list)
            current_dish=self.indices_to_dict(id)
            return make_response({"dishes":recommended_details[:8],"currentdish":current_dish,"success":1},200)
        except (ValueError, IndexError) as e:
            print(e)
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
            #if no input minutes passed, we take maximum
            if (input_minutes==""):
                input_minutes=self.maxtime
            input_minutes=int(input_minutes)
            #converting the ingredient input into a set
            input_ingredients_set = set()
            for i in input_ingredients.split(','):
                input_ingredients_set.add(i.strip().lower())
            if (len(input_ingredients_set)<2):
                return make_response({"message": "Add atleast 2 ingredients","success":0}, 200)
        except:
            return make_response({"message": "Invalid input","success":0}, 200)
        try:
            #using model to find similar dishes based on ingredients
            input_vec=self.ingredient_model_vectorizer.transform([input_ingredients])
            nearest_ingredient_dishes_distance, nearest_ingredient_dishes_indices = self.ingredient_model.kneighbors(input_vec)
            nearest_ingredient_dishes_indices=nearest_ingredient_dishes_indices.flatten().tolist()

            matching_details = []
            difference_details = []
            for index, row in self.df.iterrows():
                #converting the row ingredient into a set
                dish_ingredients_set = set([i.strip().lower() for i in row['ingredients'].split(',')])
                #filtering based on time and seeing if all the items of current row's set are in input set
                if dish_ingredients_set.issubset(input_ingredients_set) and row['minutes'] <= input_minutes:
                    matching_details.append(row.to_dict())
                    #removing filtered dishes from recommended details
                    if (index in nearest_ingredient_dishes_indices):
                        nearest_ingredient_dishes_indices.remove(index)
            
            recommended_details=self.indices_to_dict(nearest_ingredient_dishes_indices)
            for dish in recommended_details:
                #converting the row ingredient into a set
                dish_ingredients_set = set([i.strip().lower() for i in dish['ingredients'].split(',')])
                #filtering based on time
                if(dish['minutes'] <= input_minutes):
                    #taking the difference of set to set 'extra ingredients'
                    difference=dish_ingredients_set-input_ingredients_set
                    dish["difference"] = ", ".join(list(difference))
                    difference_details.append(dish)
            difference_details=sorted(difference_details, key=lambda x: x["minutes"])
            return {"dishes": matching_details,"success":1,"recommendations":difference_details}, 200
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

                #recommending dishes based on randomly selected elements
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
                return make_response({"dishes":recommended_details[:8],"wishlist":wishlist_details,"success":1}),200
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error.","success":0},200)

    
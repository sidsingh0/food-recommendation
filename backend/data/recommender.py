import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
from flask import make_response
import random

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
            if (len(wishlist)==0):
                return make_response({"message":"No items in wishlist."},204)
            if (len(wishlist)>0):
                if (len(wishlist)<3):
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
                print(combined_recommendation_list)
                for i in combined_recommendation_list:
                    row_dict = self.df.loc[self.df.index == i].to_dict(orient='records')
                    if row_dict:
                        recommended_details.append(row_dict[0])
                return make_response({"dishes":recommended_details[:8]},200)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)
    
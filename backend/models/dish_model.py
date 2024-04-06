import pandas as pd
from flask import make_response
from app import model
from scipy.sparse import hstack

class dish_model():
    
    def __init__(self):
        self.dataset=pd.read_csv('data/dishes.csv')
    
    def get_by_query(self,data):
        try:
            rows=self.dataset.head(10)
            rows_dict = rows.to_dict(orient='records')
            if (len(rows_dict)>0):
                return make_response({"dishes":rows_dict},200)
            else:
                return make_response({"message":"No dishes were found."},400)
        except Exception as e:
            return make_response({"message":"Internal server error."},500)

    def recommend(self,id):
        # try:
        input_combined_features =  hstack([description_vec[id] * 0.1, tags_vec[id] * 0.1, name_vec[id] * 0.15, ingredients_vec[id] * 0.4, numerical_features_scaled[id].reshape(1, -1) * 0.35])
        nearest_dishes_distances, nearest_dishes_indices = model.kneighbors(input_combined_features)
        print(nearest_dishes_indices)
        return make_response({"message":"done."},400)
        # except Exception as e:
        #     print(e)
        #     return make_response({"message":"Internal server error."},500)
            
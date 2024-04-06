import pandas as pd
from flask import make_response
from app import recommender

class dish_model():
    def recommend(self,id):
        return recommender.recommend(id)
            
            
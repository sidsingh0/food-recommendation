import pandas as pd
from flask import make_response
from app import recommender

class dish_model():

    def recommend_model(self,id):
        return recommender.recommend(id)

    def prompt_recommend_model(self,data):
        try:
            input_ingredients=data.get("ingredients")
            input_minutes=data.get("minutes")
            return recommender.recommend_prompt(input_ingredients,input_minutes)
        except KeyError:
            return make_response({"message": "Missing required fields in input","success":0}, 200)
        except Exception as e:
            return make_response({"message":"Invalid input","success":0},200)
            
            
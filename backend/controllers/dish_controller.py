from app import app
from models.dish_model import dish_model
from flask import request

dish=dish_model()

@app.route("/dishes/recommend/<id>",methods=["GET"])
def dish_recommend(id):
    return dish.recommend(id)
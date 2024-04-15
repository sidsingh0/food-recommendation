from app import app
from models.dish_model import dish_model
from flask import request

dish=dish_model()

@app.route("/v1/dishes/recommend/<id>",methods=["GET"])
def dish_recommend(id):
    return dish.recommend_model(id)

@app.route("/v1/dishes/prompt-recommend",methods=["POST"])
def prompt_recommend():
    data = request.get_json(silent=True)
    return dish.prompt_recommend_model(data)


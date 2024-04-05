from app import app
from models.dish_model import dish_model
from flask import request

dish=dish_model()

@app.route("/dishes/get-by-params",methods=["POST"])
def dish_query():
    data = request.get_json(silent=True)
    return dish.get_by_query(data)
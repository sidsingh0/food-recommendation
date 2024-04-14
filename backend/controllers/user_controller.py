from app import app
from models.user_model import user_model
from flask import request

user=user_model()

@app.route("/user/signin", methods=["POST"])
def signin():
    data = request.get_json(silent=True)
    return user.signin_model(data)

@app.route("/user/signup",methods=["POST"])
def signup():
    data = request.get_json(silent=True)
    return user.signup_model(data)

@app.route("/user/check-wishlist/<id>", methods=["GET"])
def check_recommendation(id):
    return user.check_wishlist_model(id)

@app.route("/user/wishlist-toggle",methods=["POST"])
def wishlist_toggle():
    data = request.get_json(silent=True)
    return user.wishlist_toggle_model(data)

@app.route("/user/wishlist",methods=["GET"])
def wishlist_get():
    return user.wishlist_model()

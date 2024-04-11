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
    return user.check_wishlist(id)

@app.route("/user/wishlist-add",methods=["POST"])
def wishlist_add():
    data = request.get_json(silent=True)
    return user.wishlist_add_model(data)

@app.route("/user/wishlist-toggle",methods=["POST"])
def wishlist_toggle():
    data = request.get_json(silent=True)
    return user.wishlist_toggle_model(data)

@app.route("/user/wishlist-remove/<id>",methods=["DELETE"])
def wishlist_remove(id):
    return user.wishlist_remove_model(id)

@app.route("/user/wishlist",methods=["GET"])
def wishlist_get():
    return user.wishlist_model()

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch(id):
    data = request.get_json(silent=True)
    return user.patch_model(data,id)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete(id):
    return user.delete_model(id)

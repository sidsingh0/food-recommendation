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

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch(id):
    data = request.get_json(silent=True)
    return user.patch_model(data,id)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete(id):
    return user.delete_model(id)

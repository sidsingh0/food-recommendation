from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os

app=Flask(__name__)
bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_KEY")
jwt = JWTManager(app)

@app.route("/")
def index_page():
    return "Index page"

from controllers import *
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from waitress import serve

app=Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
app.config["JWT_SECRET_KEY"] = "jtptechnical"
jwt = JWTManager(app)

from controllers import *

if __name__ == '__main__':
   serve(app, host="0.0.0.0", port=5000)
from flask import Flask
from flask_bcrypt import Bcrypt

app=Flask(__name__)
bcrypt = Bcrypt(app)

@app.route("/")
def index_page():
    return "Index page"

from controller import *
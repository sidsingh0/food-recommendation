from app import app
from model.user_model import user_model

user_object=user_model()

@app.route("/user/signup")
def signup():
    return user_object.user_signup_model()

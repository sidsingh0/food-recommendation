from app import bcrypt 
from bson import ObjectId
from controllers.dish_controller import dish
from datetime import datetime,timedelta
from dotenv import load_dotenv
from flask import make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import json
import os
import pandas as pd
from pymongo import MongoClient
import pytz
from validators.user_validator import *

class user_model():

    def __init__(self):
        load_dotenv()
        try:
            self.client=MongoClient("mongodb://mongodb:27017")
            self.db=self.client['food']
            self.collection=self.db['users']
            print("Connection successful to MongoDB")
        except Exception as e:
            print("Error connecting to MongoDB:", e)

    def signin_model(self, data):
        try:
            user=UserSignIn(**data)
        except ValueError as e:
            return make_response({"message": e.errors()[0]['msg'].split(", ", 1)[-1]}, 200)
        except Exception as e:
            return make_response({"message":"Please fill the fields correctly.","success":0},200)
        try:
            user_details=self.collection.find_one({"username":user.username})
            if user_details:
                if bcrypt.check_password_hash(user_details["password"], user.password):
                    expire_token_time = timedelta(hours=24)
                    token = create_access_token(identity=user.username, expires_delta=expire_token_time)
                    return make_response({"message":"Authentication successful.","token":token,"success":1},200)
                else:
                    return make_response({"message":"Invalid credentials","success":0},200)
            else:
                return make_response({"message":"User not found.","success":0},200)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error.","success":0},200)

    def signup_model(self, data):
        try:
            user=UserSignUp(**data)
        except ValueError as e:
            error_messages = [error['msg'] for error in e.errors()]
            return make_response({"message": error_messages}, 200)
        except Exception as e:
            return make_response({"message":"Please fill the fields correctly."},200)
        try:
            user_details=self.collection.find_one({"email":user.email})
            if (user_details):
                return make_response({"message":"User already exists."},200)
            user_details=self.collection.find_one({"username":user.username})     
            if (user_details):
                return make_response({"message":"User already exists."},200)           
            hashed_password=bcrypt.generate_password_hash(user.password).decode('utf-8')
            insert_query=self.collection.insert_one({"email":user.email, "password":hashed_password, "name":user.name, "username":user.username})
            if insert_query.acknowledged:
                expire_token_time = timedelta(hours=24)
                token = create_access_token(identity=user.username, expires_delta=expire_token_time)
                return make_response({"message": "User created successfully","token":token,"success":1}, 200)
            else:
                return make_response({"message": "Error creating user"},200)
        except Exception as e:
            return make_response({"message":"Internal server error."},200)
    
    @jwt_required()
    def wishlist_toggle_model(self, data):
        try:
            username=get_jwt_identity()
        except:
            return make_response({"message": "Invalid token"}, 401)
        if (not username):
            return make_response({"message":"Invalid token"},401)
        try:
            dish_id=int(data.get("id"))
            df=pd.read_csv('data/dishes.csv')
            if dish_id not in df.index:
                return make_response({"message":"Invalid Dish ID"},400)
        except:
            return make_response({"message":"Invalid Dish ID"},400)
        try:
            user_details=self.collection.find_one({"username":username})
            if user_details:
                wishlist = user_details.get("wishlist", [])
                if dish_id in wishlist:
                    # Remove dish_id from the wishlist
                    wishlist.remove(dish_id)
                    self.collection.update_one({"username": username}, {"$set": {"wishlist": wishlist}})
                    return make_response({"success": 1, "message": "Removed from wishlist!", "is_in_wishlist": 0}, 200)
                else:
                    # Add dish_id to the wishlist if not already present
                    wishlist.append(dish_id)
                    self.collection.update_one({"username": username}, {"$set": {"wishlist": wishlist}})
                    return make_response({"success": 1, "message": "Added to wishlist!", "is_in_wishlist": 1}, 200)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

    @jwt_required()
    def check_wishlist_model(self, id):
        try:
            username = get_jwt_identity()
        except:
            return make_response({"message": "Invalid token","success":0}, 200)

        if not username:
            return make_response({"message": "Invalid token","success":0}, 200)

        try:
            dish_id = int(id)
        except:
            return make_response({"message": "Invalid Dish ID","success":0}, 200)

        try:
            user_details = self.collection.find_one({"username": username})
            if user_details:
                wishlist = user_details.get("wishlist", [])
                is_in_wishlist = dish_id in wishlist
                return make_response({"is_in_wishlist": is_in_wishlist,"success":1}, 200)
            else:
                return make_response({"message": "User not found","success":0}, 200)
        except Exception as e:
            print(e)
            return make_response({"message": "Internal server error.","success":0}, 200)

    @jwt_required()
    def wishlist_model(self):
        try:
            username=get_jwt_identity()
        except:
            return make_response({"message": "Invalid token"}, 401)
        if (not username):
            return make_response({"message":"Invalid token"},401)        
        try:
            user_details=self.collection.find_one({"username":username})
            if user_details:
                wishlist=user_details.get("wishlist")
                return dish.recommend_list(wishlist)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)


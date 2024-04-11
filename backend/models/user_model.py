from app import bcrypt, recommender 
from bson import ObjectId
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
            self.client=MongoClient('localhost',27017)
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
            return make_response({"message": error_messages}, 400)
        except Exception as e:
            return make_response({"message":"Please fill the fields correctly."},400)
        try:
            user_details=self.collection.find_one({"email":user.email})
            if (user_details):
                return make_response({"message":"User already exists."},409)
            hashed_password=bcrypt.generate_password_hash(user.password).decode('utf-8')
            insert_query=self.collection.insert_one({"email":user.email, "password":hashed_password, "name":user.name, "username":user.username})
            if insert_query.acknowledged:
                expire_token_time = timedelta(hours=2)
                token = create_access_token(identity=user.username, expires_delta=expire_token_time)
                # token=create_access_token(user.username)
                return make_response({"message": "User created successfully","token":token}, 200)
            else:
                return make_response({"message": "Error creating user"},500)
        except Exception as e:
            return make_response({"message":"Internal server error."},500)
    
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
                if dish_id in user_details.get("wishlist"):
                    self.collection.update_one({"username":username},{'$pull': {'wishlist': dish_id}})
                    return make_response({"success":1,"message":"Removed from wishlist!","is_in_wishlist":0},200)
                else:
                    self.collection.update_one({"username":username},{'$addToSet': {'wishlist': dish_id}})
                    return make_response({"success":1,"message":"Added to the wishlist!","is_in_wishlist":1},200)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

    @jwt_required()
    def wishlist_add_model(self, data):
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
                self.collection.update_one({"username":username},{'$addToSet': {'wishlist': dish_id}})
                return make_response({"message":"Added to the wishlist!"},200)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

    @jwt_required()
    def wishlist_remove_model(self, id):
        try:
            username=get_jwt_identity()
        except:
            return make_response({"message": "Invalid token"}, 401)
        if (not username):
            return make_response({"message":"Invalid token"},401)
        try:
            dish_id=int(id)
        except:
            return make_response({"message":"Invalid Dish ID"},400)
        try:
            user_details=self.collection.find_one({"username":username})
            if user_details:
                self.collection.update_one({"username":username},{'$pull': {'wishlist': dish_id}})
                return make_response({"message":"Removed from the wishlist."},200)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

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
                return recommender.recommend_list(wishlist)
            else:
                return make_response({"message":"User not found"},404)
        except Exception as e:
            print(e)
            return make_response({"message":"Internal server error."},500)

    @jwt_required()
    def check_wishlist(self, id):
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



    def patch_model(self,data,id):
        try:
            update_query = {"$set": data}
            return make_response({"data":data},200)
            self.collection.update_one({"_id": ObjectId(id)}, update_query)
            return make_response({"message": "User Updated Successfully"}, 200)
        except Exception as e:
            return make_response({"message":"Internal server error."},500)
    
    def delete_model(self,id):
        try:
            result = self.collection.delete_one({"_id": id})
            if result.deleted_count > 0:
                return make_response({"message": "User Deleted Successfully"}, 200)
            else:
                return make_response({"message": "Nothing to delete"}, 400)
        except Exception as e:
            return make_response({"message": str(e)}, 400)


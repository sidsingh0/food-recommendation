from app import bcrypt
from bson import ObjectId
from datetime import datetime
from flask import make_response
import json
import jwt
import os
from pymongo import MongoClient

class user_model():

    def __init__(self):
        try:
            self.client=MongoClient('localhost',27017)
            self.db=self.client['food']
            self.collection=self.db['users']
            print("Connection successful to MongoDB")
        except Exception as e:
            print("Error connecting to MongoDB:", e)

    def signin_model(self, data):
        try:
            if not data or "email" not in data or "password" not in data:
                return make_response({"message":"Please enter both email and password."},400)
            email=data.get("email")
            password=data.get("password")
            user_details=self.collection.find_one({"email":email})
            if user_details:
                if bcrypt.check_password_hash(user_details["password"], password):
                    expiry_time=datetime.now()+timedelta(hours=24)
                    epoch_expiry_time=int(expiry_time.timestamp())
                    token=jwt.encode({"email":email,"expiry":epoch_expiry_time},os.getenv("JWT_KEY"),os.getenv("JWT_ALGORITHM"))
                    return make_response({"message":"Authentication successful.","token":token},200)
                else:
                    return make_response({"message":"Invalid credentials"},400)
            else:
                return make_response({"message":"User not found."},400)
        except Exception as e:
                return make_response({"message":"Internal server error."},500)

    def signup_model(self, data):
        try:
            self.collection.insert_one(data)
            return make_response({"message": "User Created Successfully"}, 200)
        except Exception as e:
            return make_response({"message":"Internal server error."},500)

    def patch_model(self,data,id):
        try:
            update_query = {"$set": data}
            self.collection.update_one({"_id": ObjectId(id)}, update_query)
            return make_response({"message": "User Updated Successfully"}, 200)
        except Exception as e:
            return make_response({"message": str(e)}, 400)
    
    def delete_model(self,id):
        try:
            result = self.collection.delete_one({"_id": id})
            if result.deleted_count > 0:
                return make_response({"message": "User Deleted Successfully"}, 200)
            else:
                return make_response({"message": "Nothing to delete"}, 400)
        except Exception as e:
            return make_response({"message": str(e)}, 400)

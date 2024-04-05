from pydantic import BaseModel, EmailStr, validator
import re

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    name: str
    username: str
    
    @validator('name')
    def validate_name(cls, value):
        regex = r'^[a-zA-Z\s]+$'
        if not re.match(regex, value) or len(value) >= 50 or len(value)<1:
            raise ValueError("Name must be alphabetic and less than 50 characters")
        return value

    @validator('username')
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric.")
        if len(value)>=20:
            raise ValueError("Username must be less than 20 characters.")
        return value

    @validator('password')
    def validate_password(cls, value):
        regex = r'^[a-zA-Z0-9]+$'
        if not re.match(regex, value):
            raise ValueError("Password must be alphanumeric and less than 50 characters and more than 6 characters")
        if len(value) >= 50:
            raise ValueError("Password should be less than 50 characters.")
        if len(value)<6:
            raise ValueError("Password should be more than 6 characters.")
        return value

class UserSignIn(BaseModel):
    password: str
    username: str

    @validator('username')
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric.")
        if len(value)>=20:
            raise ValueError("Username must be less than 20 characters.")
        return value
        
    @validator('password')
    def validate_password(cls, value):
        regex = r'^[a-zA-Z0-9]+$'
        if not re.match(regex, value):
            raise ValueError("Password must be alphanumeric and less than 50 characters and more than 6 characters")
        if len(value) >= 50:
            raise ValueError("Password should be less than 50 characters.")
        if len(value)<6:
            raise ValueError("Password should be more than 6 characters.")
        return value

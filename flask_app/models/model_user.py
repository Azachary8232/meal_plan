

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
model_db = "meals"


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#   To VALIDATE USER REGISTRATION Info
    @staticmethod
    def validate_user_registration(user):
        is_valid = True
        if len(user['first_name']) < 1: 
            flash("A First Name must be included.", category= "reg_first_name")
            is_valid = False  
        if len(user['last_name']) < 1: 
            flash("A Last Name must be included.", category= "reg_last_name")
            is_valid = False  
        if not EMAIL_REGEX.match(user['email']): 
            flash("Please enter a valid Email.", category= "reg_email")
            is_valid = False
        if len(user['password']) < 1: 
            flash("A Password must be included.", category= "reg_password")
            is_valid = False  
        if user['password'] != user['confirm_password']: 
            flash("Passwords do not match.", category= "reg_confirm_password")
            is_valid = False  
        return is_valid

#   To VALIDATE USER LOGIN Credentials
    @staticmethod
    def validate_user_login(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Please enter a valid Email.", category= "login_email")
            is_valid = False
        if len(user['password']) < 1: 
            flash("Please enter a password.", category= "login_password")
            is_valid = False  
        return is_valid

    # ***CREATE***

    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(model_db).query_db(query, data)




    # ***Retreive***

    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(model_db).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])




    # ***Update***







    # ***Delete***
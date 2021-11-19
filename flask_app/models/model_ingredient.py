from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 


model_db = "meals"


class Meal:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_new_ingredient(data):
        is_valid = True
        if len(data['name']) < 1: 
            flash("Please add Ingredient name.", category= "new_ingredient_name")
            is_valid = False  
        return is_valid




    # ***CREATE***





            # ***Retreive***




    # ***Update***





    # ***Delete***
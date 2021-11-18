

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 

model_db = "meals"


class Meal:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.directions = data['directions']
        self.meal_time = data['meal_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_new_meal(meal):
        is_valid = True
        if len(meal['name']) < 1: 
            flash("Please name your meal.", category= "new_meal_name")
            is_valid = False  
        return is_valid


    # ***CREATE***

    @classmethod
    def create_meal(cls,data):
        query = "INSERT INTO meals (name, directions, meal_time, user_id) VALUES (%(name)s, %(directions)s, %(meal_time)s, %(user_id)s);"
        meal_id =  connectToMySQL(model_db).query_db(query, data)
        return meal_id


            # ***Retreive***





    # ***Update***







    # ***Delete***


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
        self.prep_time = data['prep_time']
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

    @classmethod
    def get_meal_by_id(cls,data):
        query = "SELECT * FROM meals WHERE id = %(id)s;"
        meal = connectToMySQL(model_db).query_db(query,data)
        print(meal)
        return cls(meal[0])




    # ***Update***

    @classmethod
    def update_directions(cls, data):
        query = 'UPDATE meals SET directions = %(directions)s, prep_time = %(prep_time)s WHERE id = %(id)s';
        connectToMySQL(model_db).query_db(query, data)
        return print("Update Successful")





    # ***Delete***
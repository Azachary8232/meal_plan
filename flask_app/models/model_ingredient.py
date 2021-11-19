from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 


model_db = "meals"


class Ingredient:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.store_id = data['store_id']

    @staticmethod
    def validate_new_ingredient(data):
        is_valid = True
        if len(data['name']) < 1: 
            flash("Please add Ingredient name.", category= "new_ingredient_name")
            is_valid = False  
        return is_valid




    # ***CREATE***

    @classmethod
    def create_ingredient(cls,data):
        query = "INSERT INTO ingredients (name, store_id) VALUES (%(name)s, %(store_id)s);"
        ingredient_id =  connectToMySQL(model_db).query_db(query, data)
        return ingredient_id

    @classmethod
    def create_user_has_ingredient(cls,data):
        query = "INSERT INTO users_has_ingredients (user_id, ingredient_id) VALUES (%(user_id)s, %(ingredient_id)s);"
        results =  connectToMySQL(model_db).query_db(query, data)
        return results

    @classmethod
    def create_meals_ingredients(cls,data):
        query = "INSERT INTO meals_ingredients (meal_id, ingredient_id) VALUES (%(meal_id)s, %(ingredient_id)s);"
        results =  connectToMySQL(model_db).query_db(query, data)
        return results



            # ***Retreive***




    # ***Update***





    # ***Delete***
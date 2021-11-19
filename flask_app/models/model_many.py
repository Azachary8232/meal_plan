from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
from flask_app.models import model_ingredient

model_db = "meals"



class Meals_ingredients:
    def __init__(self,data):
        self.meal_id = data['meal_id']
        self.ingredient_id = data['ingredient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#    *****Create*****

    @classmethod
    def create_meals_ingredients(cls,data):
        query = "INSERT INTO meals_ingredients (meal_id, ingredient_id) VALUES (%(meal_id)s, %(ingredient_id)s);"
        results =  connectToMySQL(model_db).query_db(query, data)
        return results

#       **** Retrieve ****





class Users_has_ingredients:
    def __init__(self,data):
        self.user_id = data['user_id']
        self.ingredient_id = data['ingredient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#       **** Create ****

    @classmethod
    def create_user_has_ingredient(cls,data):
        query = "INSERT INTO users_has_ingredients (user_id, ingredient_id) VALUES (%(user_id)s, %(ingredient_id)s);"
        results =  connectToMySQL(model_db).query_db(query, data)
        return results


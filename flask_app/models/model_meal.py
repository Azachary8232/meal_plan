

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
from flask_app.models import model_ingredient

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
        return cls(meal[0])

    @classmethod
    def get_ingredients_by_meal_id(cls,data):
        query = "SELECT * FROM meals JOIN meals_ingredients ON meals.id = meals_ingredients.meal_id JOIN ingredients ON meals_ingredients.ingredient_id = ingredients.id WHERE meals.id = %(id)s;"
        results = connectToMySQL(model_db).query_db(query,data)
        meal = cls(results[0])
        meal.ingredients = []
        for row in results:
            ingredient_data = {
                'id' : row['ingredients.id'],
                'name' : row['ingredients.name'],
                'created_at' : row['ingredients.created_at'],
                'updated_at' : row['ingredients.updated_at'],
                'store_id' : row['store_id']
            }
            meal.ingredients.append(model_ingredient.Ingredient(ingredient_data) )
        return meal



    # ***Update***

    @classmethod
    def update_directions(cls, data):
        query = 'UPDATE meals SET directions = %(directions)s, prep_time = %(prep_time)s WHERE id = %(id)s';
        connectToMySQL(model_db).query_db(query, data)
        return print("Update Successful")





    # ***Delete***
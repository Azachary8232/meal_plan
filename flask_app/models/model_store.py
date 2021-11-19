from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 


model_db = "meals"


class Store:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_new_store(store):
        is_valid = True
        if len(store['name']) < 1: 
            flash("Please enter a Store.", category= "new_store_name")
            is_valid = False  
        return is_valid




#      ***CREATE***

    @classmethod
    def create_store(cls,data):
        query = "INSERT INTO stores (name, user_id) VALUES (%(name)s, %(user_id)s);"
        meal_id =  connectToMySQL(model_db).query_db(query, data)
        return meal_id





            # ***Retreive***

    @classmethod
    def get_store_by_user_id(cls,data):
        query = "SELECT * FROM stores WHERE user_id = %(id)s;"
        results = connectToMySQL(model_db).query_db(query,data)
        print(results)
        return results










    # ***Update***









    # ***Update***

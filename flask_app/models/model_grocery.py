from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
from flask_app.models import model_ingredient

model_db = "meals"


class Grocery:
    def __init__(self,data):
        self.id = data['id']
        self.ingredient_id = data['ingredient_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']




    # ***CREATE***

    @classmethod
    def create_list(cls,data):
        query = "INSERT INTO grocery_list (ingredient_id, user_id) VALUES (%(ingredient_id)s, %(user_id)s);"
        grocery_id =  connectToMySQL(model_db).query_db(query, data)
        return grocery_id




            # ***Retreive***


    # ***Update***




    # ***Delete***
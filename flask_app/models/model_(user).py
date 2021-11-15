# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 
import re
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 





class (User)/no():
    def __init__(self,data):
        self.id = data['id']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ***CREATE***






    # ***Retreive***






    # ***Update***







    # ***Delete***
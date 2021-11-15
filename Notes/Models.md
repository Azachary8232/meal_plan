## Models
```py
# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
model_db = 'SAMPLE'

class (User)/no():
    def __init__(self,data):
        self.id = data['id']
```
##                   ***Create***
```py
    @classmethod
def create(cls,data):
    query = "INSERT INTO (users/no()) (*something*, *something*) VALUES (%(*something*)s, %(*something*)s);"
    (user/no())_id = connectToMySQL('model_db').query_db(query,data)
    return (user/no())_id
```
##                    ***Retreive***
```py
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM (users)/no());"
        results = connectToMySQL('model_db').query_db(query)
        (userS/no()) = []
        for user in results:
            (userS/no()).append(cls(user))
        return (userS/no()) 

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('model_db').query_db(query,data)

        return cls(burger_from_db[0])

	# (joining two groups)  
    # add... from .model_(user/no()) import (User/no()) **to top of page 
	# add... self.(users/no()) = [] **to class(User/no()):
    @classmethod
    def get_one_with_ninjas(cls, data ):
        print(data)
        query = "SELECT * FROM (userS/no()) LEFT JOIN ninjas on (userS/no()).id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('***userS***').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # users = [] in self dictionary
            dojo.(userS/no()).append( ***User***(n) )
        return dojo
```
##                  ***Update***
```py
@classmethod
def update(cls, data)
    query = 'UPDATE *users* SET first_name = %(first_name)s, last_name = %(last_name)s WHERE id = %(id)s';
    connectToMySQL(model_db).query_db(query, data)
    return print("Update Successful")


```
##                  ***Delete***
```py
@classmethod
def delete(cls,data):
    query = 'DELETE FROM *users* WHERE id = %(id)s';
    connectToMySQL(model_db).query_db(query, data)
    return print("Delete Successful")



```
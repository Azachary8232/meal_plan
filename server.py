from flask_app.controllers import controller_users, controller_meals, controller_stores, controller_ingredients, controller_grocery 
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)
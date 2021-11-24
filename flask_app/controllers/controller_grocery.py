from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal, model_store, model_ingredient, model_many, model_grocery



#  From MY MEALS list CREATE GROCERY LIST
@app.route('/grocery_list/<int:id>')
def grocery_list(id):
    data = { 'id' : id }
    meal = model_meal.Meal.get_ingredients_by_meal_id(data)
    for item in meal.ingredients:
        print(item)
        data = { 
            'ingredient_id' : item.id,
            'user_id' : session['user_id']
            }
        model_grocery.Grocery.create_list(data)
    return redirect('/dashboard')
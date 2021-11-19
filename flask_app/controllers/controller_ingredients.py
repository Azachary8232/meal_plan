
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal, model_store, model_ingredient, model_many




#   from ***ADD MEAL*** INGREDIENTS FORM to ADD INGREDIENT 
@app.route('/add_ingredient/<int:meal_id>', methods = ['POST'])
def add_ingredient(meal_id):
    if not model_ingredient.Ingredient.validate_new_ingredient(request.form):
        return redirect(f'/add_meal/{meal_id}')

    data = {
        'name' : request.form['name'],
        'store_id' : request.form['store_id']
    }
    ingredient_id = model_ingredient.Ingredient.create_ingredient(data)

    data2 = {
        'user_id' : session['user_id'],
        'ingredient_id' : ingredient_id,
    }
    model_many.Users_has_ingredients.create_user_has_ingredient(data2)

    data3 = {
        'meal_id' : meal_id,
        'ingredient_id' : ingredient_id
    }
    model_many.Meals_ingredients.create_meals_ingredients(data3)
    return redirect(f'/add_meal/{meal_id}')


    #   from ***EDIT*** INGREDIENTS FORM to ADD INGREDIENT 
@app.route('/add_ingredients/<int:meal_id>', methods = ['POST'])
def add_ingredients(meal_id):
    if not model_ingredient.Ingredient.validate_new_ingredient(request.form):
        return redirect(f'/add_meal/{meal_id}')

    data = {
        'name' : request.form['name'],
        'store_id' : request.form['store_id']
    }
    ingredient_id = model_ingredient.Ingredient.create_ingredient(data)

    data2 = {
        'user_id' : session['user_id'],
        'ingredient_id' : ingredient_id,
    }
    model_many.Users_has_ingredients.create_user_has_ingredient(data2)

    data3 = {
        'meal_id' : meal_id,
        'ingredient_id' : ingredient_id
    }
    model_many.Meals_ingredients.create_meals_ingredients(data3)
    return redirect(f'/edit_meal/{meal_id}')


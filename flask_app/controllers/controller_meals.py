
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal, model_store, model_ingredient, model_many



#  Route to USERS MEALS
@app.route('/meals')
def meals():
    if 'user_id' not in session:
        return redirect('/login')

    id = { 'id' : session['user_id']}
    meals = model_meal.Meal.get_all_by_user(id)

    return render_template('my_meals.html', meals = meals)

#  Route to CREATE NEW MEAL
@app.route('/new_meal')
def add_meal():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('create_meal.html')

#   from FORM to CREATE NEW MEAL
@app.route('/create_meal', methods = ['POST'])
def creat_meal():
    if not model_meal.Meal.validate_new_meal(request.form):
        return redirect('/new_meal')
    
    data = {
        'name' : request.form['name'],
        'directions' : request.form['directions'],
        'meal_time' : request.form['meal_time'],
        'user_id' : session['user_id']
    }
    meal_id = model_meal.Meal.create_meal(data)
    return redirect(f'/add_meal/{meal_id}')

#   Route to ADD INGREDIENTS and DIRECTIONS to USER MEAL
@app.route('/add_meal/<int:id>')
def add(id):
    if 'user_id' not in session:
        return redirect('/login')
#       Adding store to dropdown
    user_id = { 'id' : session['user_id']}
    stores = model_store.Store.get_store_by_user_id(user_id)

    id = {'id' : id}
    ingredients = model_meal.Meal.get_ingredients_by_meal_id(id)
    meal = model_meal.Meal.get_meal_by_id(id)
    return render_template('add_meal.html', meal = meal, stores = stores, ingredients = ingredients)

#  from DIRECTIONS FORM to UPDATE MEAL
@app.route('/directions_update/<int:id>', methods = ['POST'])
def directions_update(id):
    data = { 
        'id' : id,
        'directions' : request.form['directions'],
        'prep_time' : request.form['prep_time']
        }

    model_meal.Meal.update_directions(data)
    return redirect(f'/add_meal/{id}')



#  Route to EDIT MEALS INFO
@app.route('/edit_meal/<int:id>')
def edit_meal(id):
    if 'user_id' not in session:
        return redirect('/login')

    data = { 'id' : id }
    ingredients = model_meal.Meal.get_ingredients_by_meal_id(data)
    meal = model_meal.Meal.get_meal_by_id(data)

    user_id = { 'id' : session['user_id'] }
    stores = model_store.Store.get_store_by_user_id(user_id)

    return render_template('edit_meal.html', meal = meal, ingredients = ingredients, stores = stores)

#  Route from FORM to UPDATE MEAL INFO 
@app.route('/update_meal/<int:id>', methods = ['POST'])
def update_meal(id):

    data = {
        'meal_time' : request.form['meal_time'],
        'name' : request.form['name'],
        'directions' : request.form['directions'],
        'prep_time' : request.form['prep_time'],
        'id' : id,
    }
    model_meal.Meal.update_meal(data)

    return redirect(f'/edit_meal/{id}')





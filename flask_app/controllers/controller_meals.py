
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal



#  Route to USERS MEALS
@app.route('/meals')
def meals():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('my_meals.html')

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

    meal_id = {'id' : id}
    meal = model_meal.Meal.get_meal_by_id(meal_id)
    return render_template('add_meal.html', meal = meal)

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
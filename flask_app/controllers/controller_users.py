# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/meals')
def meals():
    return render_template('my_meals.html')

@app.route('/edit_meal')
def edit():
    return render_template('edit_meal.html')

@app.route('/add_meal')
def add():
    return render_template('add_meal.html')
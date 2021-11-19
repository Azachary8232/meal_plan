from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal, model_store





@app.route('/add_store')
def add_store():
    if 'user_id' not in session:
        return redirect('/login')


    return render_template('add_store.html')


@app.route('/create_store', methods = ['POST'])
def create_store():
    model_store.Store.validate_new_store(request.form)

    data = {
        'name' : request.form['name'],
        'user_id' : session['user_id']
    }

    model_store.Store.create_store(data)
    return redirect('/add_store')
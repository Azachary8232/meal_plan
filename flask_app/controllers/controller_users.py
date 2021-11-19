# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_user, model_meal, model_store
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)




#  First Stop Index Page
@app.route('/')
def index():
    return render_template('login.html')

#  From GUEST PAGE to LOGIN
@app.route('/guest_login')
def guest_login():
    return render_template('guest_login.html')

#   from FORM to LOGIN USER
@app.route('/login', methods = ['POST'])
def user_login():
    if not model_user.User.validate_user_login(request.form):
        return redirect('/')

    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = model_user.User.get_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", category= "user_email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", category= "user_email")
        return redirect('/')

    session['user_id'] = user_in_db.id
    print(session['user_id'])
    return redirect('/dashboard')



#   Route To REGISTRATION page
@app.route('/registration')
def user_registration():
    return render_template('user_registration.html')
    
#   from FORM to REGISTER NEW USER
@app.route('/register', methods= ['POST'])
def register():
    if not model_user.User.validate_user_registration(request.form):
        return redirect('/registration')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    user_id = model_user.User.create_user(data)
    session['user_id'] = user_id

    return redirect('/dashboard')


#  Route FROM Login/Registration TO DASHBOARD
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template("dashboard.html")





    
@app.route('/edit_meal')
def edit():
    return render_template('edit_meal.html')



#  ROUTE For USER to LOGOUT
@app.route('/logout')
def user_logout():
    session.clear()
    return redirect('/')
```py
##                                Validation
```

##          ***Validate for Correcect Input Fields***
```py
#models
@staticmethod
def validate_user(user):
    is_valid = True # we assume this is true

    # for ***Text Input*** unknown
    if len(user['first_name']) < 1: 
        flash("first_name must be included.", category= "user_SAMPLE")
        is_valid = False  #-- use different if statement for all inputs
    return is_valid

    # for ***Select/Options Input***
    if len(ninja['location']) < 2: 
        flash("Language must be included.", category= "user_SAMPLE")
        is_valid = False  #-- use different if statement for all inputs
    return is_valid

    # for ***EMAIL***
    import re	# the regex module  <--- add to /model top
    # create a regular expression object that we'll use later   
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top

    if not EMAIL_REGEX.match(user['email']): 
        flash("Invalid email address!", category= "user_SAMPLE")
        is_valid = False
    return is_valid


#contoller

# For ***Registration***

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    data = {
        "username": request.form['username'],
    }
    user_id = User.create(data)
    session['user_id'] = user_id

    return redirect('/dashboard')

# *** For Form Correctness***

@app.route('/create', methods=['POST'])
def create():
    if not User.vaildate_info(request.form):
        return redirect('/')

#HTML
{% with messages = get_flashed_messages(category_filter= 'user_SAMPLE') %}    
    {% if messages %}                           
        {% for message in messages %}            
            <p>{{message}}</p>                 
        {% endfor %}
    {% endif %}
{% endwith %}

```

## User_Name / Password Registration
```py
# In controller

from flask_app import app   #<--- Install to top of controller
from flask_bcrypt import Bcrypt  #<---- Install to top of controller
bcrypt = Bcrypt(app)

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    if not User.validate_user(request.form):
    return redirect('/')

    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")

# In Model

class User:
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s);"
        return connectToMySQL("mydb").mysql.query_db(query, data)
```

##  To Check User_name / Password Login
```py
# In Controller

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { 
        "email" : request.form["email"] 
        }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", category= "email")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", category= "email)
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")

# In Model

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])


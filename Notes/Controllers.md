## Controllers
```py
# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.(user/no()) import (User/no())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        # 'id' : id
        "(something/no())" : request.form['(somethong/no())'],
        "(something/no())" : request.form['(somethong/no())'],
    }
    Sample.create(data)
    return redirect('/sample')

# Left Join --- Works with models 'get_one_with_....'
@app.route('/sample/<int:id>')
def sample(id):
    data = {
    "id": id
    }
    return render_template('dojo_info.html', dojo=Dojo.get_one_with_ninjas(data))   




```
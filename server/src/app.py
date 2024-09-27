# Two ways of running flask:

# flask --app src/app.py run --port 5555 --debug

# API == Application Programming Interface
# HTTP == common protocol
# REST == Representational State Transfer
#   - useful design pattern for APIs

import os
import traceback
from flask import Flask, request, session
from flask_migrate import Migrate
from models import db, Pet, PetException, User
from flask_cors import CORS


# initialize our flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set the secret key (needed for cookies)
app.secret_key = os.environ['SECRET_KEY']

# initialize sqlalchemy plugin with flask
db.init_app(app)
# initialize Alembic (aka flask migrate)
Migrate(app, db)

# set up CORS
# CORS(app, supports_credentials=True)
CORS(app)


# define flask views (will connect to react routes)
@app.route('/')
def root():
    # returning an html response
    return '<h1>hello world!</h1>', 200  # status code 200 == ok

@app.route('/test')
def test():
    # returning json reponse (very useful for APIs)
    json_data = {
        'key': 'value',
        'test': [1, 2, 3]
    }
    return json_data, 200


# we can parameterize our url strings with flask
@app.route('/api/users')
def all_users():
    pass

@app.route('/api/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def users_by_id():
    pass

@app.route('/api/applicants')
def all_students():
    pass

@app.route('/api/applicants/<int:id>', methods=["GET", "PATCH", "DELETE"])
def student_by_id():
    pass

@app.route('/api/applications')
def all_applications():
    pass

@app.route('/api/applications/<int:id>', methods=["GET", "PATCH", "DELETE"])
def applications_by_id():
    pass

@app.route('/api/apply', methods=['POST'])
def apply():
    pass

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    # query the database by username
    user = User.query.filter(User.username == data.get('username')).first()

    # check if user exists
    if user is None:
        return {'error': 'login failed'}, 401
    
    # checking if the password matches
    if not user.authenticate(data.get('password')):
        return {'error': 'login failed'}, 401
    
    # set a browser cookie
    session['user_id'] = user.id
    
    return user.to_dict(), 200

@app.route('/api/logout', methods=['DELETE'])
def logout():
    # delete the cookie
    session.pop('user_id', None)
    return {'message': 'logout success'}, 200



@app.route('/api/check_session', methods=['GET'])
def check_session():
    """Check if the user is already logged in"""
    # get the user_id cookie
    user_id = session.get('user_id')

    # query the db for a user with this id
    user = User.query.filter(User.id == user_id).first()

    # make sure the user exists in the db
    if user is None:
        # return error code if not
        return {'error': 'unauthorized'}, 401
    
    # return success code 
    return user.to_dict(), 200

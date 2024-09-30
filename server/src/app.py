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
from models import db, Application, Student, School, User, ApplicationException, StudentException
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

@app.route('/api/users/<string:type>', methods=["GET"])
def applicants():
    """Can specifically access Applicant users, i.e. so Staff-type users can see data for an Applicant who has many Students"""
    pass

@app.route('/api/schools', methods=["GET"])
def all_schools():
    if request.method == "GET":
        schools = School.query.all()
        return [school.to_dict() for school in schools], 200

@app.route('/api/schools/<int:id>', methods=["GET"])
def school_by_id(id):
    school = School.query.filter(School.id == id).first()
    if school is None:
        return {"error": "school not found"}, 404
    
    if request.method == "GET":
        return school.to_dict(), 200

@app.route('/api/students', methods=["GET", "POST"])
def all_students():
    if request.method == "GET":
        students = Student.query.all()
        return [stud.to_dict() for stud in students], 200
    if request.method == "POST":
        data = request.get_json()
        #Circle back to validation, examples below though...
        if 'first_name' not in data:
            return {"error": "first name is required"}, 400
        if 'last_name' not in data:
            return {"error": "last name is required"}, 400
        if 'dob' not in data:
            return {"error": "date of birth is required"}, 400
        try:
            new_student = Student(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                dob=data.get('dob'),
                age=data.get('age'),
                expected_grade_level=data.get('expected_grade_level'),
                user_relationship=data.get('user_relationship')
            )
        except StudentException as e:
            print(traceback.format_exc())
            return {'error': str(e)}, 400
        
        db.session.add(new_student)
        db.session.commit()

        return new_student.to_dict(), 201

@app.route('/api/students/<int:id>', methods=["GET", "PATCH"])
def student_by_id(id):
    stud = Student.query.filter(Student.id == id).first()
    if stud is None:
        return {"error": "student not found"}, 404
    
    if request.method == "GET":
        return stud.to_dict(), 200
    
    if request.method == "PATCH":
        pass

@app.route('/api/applications', methods=["GET", "POST"])
def all_applications():
    if request.method == "GET":
        applications = Application.query.all()
        return [appl.to_dict() for appl in applications], 200
    if request.method == "POST":
        data = request.get_json()
        #Circle back to validation, examples below though...
        if 'student' not in data:
            return {"error": "student is required"}, 400
        if 'school' not in data:
            return {"error": "school is required"}, 400
        if 'user_signature' not in data:
            return {"error": "user signature is required"}, 400
        try:
            new_application = Application(
                student=data.get('student'),
                school=data.get('school'),
                user=data.get('user'),
                user_signature=data.get('user_signature')
            )
        except ApplicationException as e:
            print(traceback.format_exc())
            return {'error': str(e)}, 400
        
        db.session.add(new_application)
        db.session.commit()

        return new_application.to_dict(), 201


@app.route('/api/applications/<int:id>', methods=["GET", "DELETE"])
def applications_by_id(id):
    appl = Application.query.filter(Application.id == id).first()
    if appl is None:
        return {"error": "application not found"}, 404
    
    if request.method == "GET":
        return appl.to_dict(), 200
    
    if request.method == "DELETE":
        db.session.delete(appl)
        db.session.commit()

        return {}, 204

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

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# init sqlalchemy object
db = SQLAlchemy(metadata=MetaData(naming_convention=convention))

# init bcrypt plugin
bcrypt = Bcrypt()

# create exception class for validation
class PetException(Exception):
    pass

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'  # tablename is required

    __table_args__ = (db.CheckConstraint('age >= 0', name='ck_age_not_neg'), )

    # define columns on our table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False) #Ben said this should work, but need to test and confirm... might be datetime
    user_relationship = db.Column(db.String, nullable=False) # need to validate, options are Mother, Father, Specify Other Guardian ___
    age = db.Column(db.Integer, nullable=False)
    expected_grade_level = db.Column(db.String) # PreK, Kindergarten, 1st grade, etc.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # fk for for users, i.e. parents

    # relationship needs the class name (as a str)
    user = db.relationship('User', back_populates='students')

    # serialization rules
    serialize_rules = ('-user.students',) # -owner_id is optiona
    # serialize_only = ['name']

#JB note to revisit validates...
    # @validates('age')
    # def validates_age(self, key, new_age):
    #     if new_age < 0:
    #         raise PetException('age cannot be negative')
    #     return new_age  # similar to self._age = new_age

    def __repr__(self) -> str:
        return f'<Student {self.id} {self.first_name} {self.last_name} {self.age} {self.expected_grade_level}>'
    
# Classes JB will actually use!!!
class Application(db.Model, SerializerMixin):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id')) 
    school_choice = db.Column(db.String, nullable=False) # for now, Alpha School, Beta School, etc
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_signature = db.Column(db.String, nullable=False) # user types name, validate matches name from user_id pulled from users table

    students = db.relationship('Student', back_populates='application')
    users = db.relationship('User', back_populates='application')

    serialize_rules = ['-student.application', '-user.application']

    def __repr__(self) -> str:
        return f'<Application {self.id} {self.student_id} {self.school_choice}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String)
    user_type = db.Column(db.String, nullable=False) # Applicant vs Staff
    staff_type = db.Column(db.String, nullable=True) # General vs Priveleged

    students = db.relationship('Student', back_populates="user")
    applications = db.relationship('Application', back_populates="user")

    serialize_rules = ['-password_hash', '-application.user', '-student.user']

    @hybrid_property
    def password(self):
        """Returns the password hash"""
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        """Hashes the plain text password"""
        bytes = plain_text_password.encode('utf-8')  # convert our string into raw bytes
        self.password_hash = bcrypt.generate_password_hash(bytes)  # hash the bytes

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self.password_hash,  # hashed password
            password.encode('utf-8')  # plain text password
        )

    def __repr__(self) -> str:
        return f'<User {self.id} {self.username}>'
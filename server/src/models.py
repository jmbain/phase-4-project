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

# EXAMPLE PET MODEL - for reference to start, delete later
class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'  # tablename is required

    __table_args__ = (db.CheckConstraint('age >= 0', name='ck_age_not_neg'), )

    # define columns on our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    type = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))  # fk for owners.id

    # relationship needs the class name (as a str)
    owner = db.relationship('Owner', back_populates='pets')

    # serialization rules
    serialize_rules = ('-owner.pets',) # -owner_id is optional
    # serialize_only = ['name']

    @validates('age')
    def validates_age(self, key, new_age):
        if new_age < 0:
            raise PetException('age cannot be negative')
        return new_age  # similar to self._age = new_age

    def __repr__(self) -> str:
        return f'<Pet {self.id} {self.name} {self.age}>'
    
# Classes JB will actually use!!!
class Application(db.Model, SerializerMixin):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    sat_score = db.Column(db.Integer,)

    pets = db.relationship('Pet', back_populates='owner')

    serialize_rules = ['-pets.owner']

    def __repr__(self) -> str:
        return f'<Owner {self.id} {self.name}>'


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String)
    user_type = db.Column(db.String, nullable=False) # Applicant vs Staff
    staff_type = db.Column(db.String, nullable=True) # General vs Priveleged


    serialize_rules = ['-password_hash']

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
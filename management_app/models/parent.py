from management_app.config.db import db
from management_app import bcrypt
from flask import flash

class Parent(db.Model):
    __tablename__ = 'parents'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    password = db.Column(db.String(60))
    
    # Foreign Keys
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data:dict):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.users_id = data['users_id']

    @classmethod
    def create(cls, data:dict):
        parent = cls({
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': cls.hash_password(data['password']),
            'users_id': data['users_id']
        })
        db.session.add(parent)
        db.session.commit()
        return parent

    @classmethod
    def login(cls, dict:dict):
        print("running login function")
        parent = cls.query.filter_by(email=dict['email']).first()
        if parent and cls.check_password(dict['password'], parent.password):
            return parent
        
        print('Invalid email or password')
        flash('Invalid email or password', 'error')
        return None

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def check_password(password, hashed_password):
        return bcrypt.check_password_hash(hashed_password, password)
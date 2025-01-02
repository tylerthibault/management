from .. import db
from datetime import datetime
from management import bcrypt
from flask import flash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    role = db.Column(db.String(20), nullable=False)
    
    # Foreign key to organization
    org_id = db.Column(db.Integer, db.ForeignKey('orgs.id'))

    def __repr__(self):
        return f'<User {self.email}>'

    @classmethod
    def create(cls, data: dict):
        data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        user = cls(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def authenticate(cls, data: dict, type="login"):
        is_valid = True

        if type == "login":
            if not data['email'] or not data['password']:
                is_valid = False
                flash('Please provide email and password')

        user = cls.query.filter_by(email=data['email']).first()
        if not user:
            is_valid = False
            flash('User not found')

        if user and not bcrypt.check_password_hash(user.password, data['password']):
            is_valid = False
            flash('Invalid password')

        return user if is_valid else False

        
        
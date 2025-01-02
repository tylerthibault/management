from .. import db
from datetime import datetime
from management.models.user import User
from flask import flash
from management import bcrypt

class Org(db.Model):
    __tablename__ = "orgs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    # Relationship with users
    users = db.relationship('User', backref='org', lazy=True)

    def __repr__(self):
        return f'<Organization {self.name}>'

    @classmethod
    def create(cls, data: dict):
        pw = data['password']
        data['password'] = bcrypt.generate_password_hash(pw).decode('utf-8')
        org = cls(**data)
        db.session.add(org)
        db.session.commit()
        
        # Create a new user with role 'admin'
        user_data = {
            'name': data['name'],
            'email': data['email'],
            'password': pw,
            'org_id': org.id,
            'role': 'sys-admin'
        }
        user = User.create(user_data)
        flash('Organization admin created successfully!')
        print(f'Organization created successfully! user_id: {user.id}')
        return org
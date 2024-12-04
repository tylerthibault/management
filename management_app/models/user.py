from datetime import datetime
from management_app.config.db import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign Keys
    families_id = db.Column(db.Integer, db.ForeignKey('families.id'), nullable=True)
    
    # Relationships
    parent = db.relationship('Parent', backref='user', uselist=False, lazy=True)
    child = db.relationship('Child', backref='user', uselist=False, lazy=True)
    family = db.relationship('Family', foreign_keys=[families_id], backref='members', lazy=True)

    def __init__(self, data:dict):
        self.role = data['role']

    @classmethod
    def create(cls, data:dict):
        user = cls({**data})
        db.session.add(user)
        db.session.commit()
        return user
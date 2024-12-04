from datetime import datetime
from management_app.config.db import db

class Family(db.Model):
    __tablename__ = 'families'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    code = db.Column(db.String(10))
    
    # Foreign Keys
    head_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    head_user = db.relationship('User', backref='headed_families', uselist=False, foreign_keys=[head_user_id])

    def __init__(self, data:dict):
        self.name = data['name']
        self.code = data['code']
        self.head_user_id = data['head_user_id']

from datetime import datetime, timedelta
from management_app.config.db import db
from flask import session
import secrets

class LoginRecord(db.Model):
    __tablename__ = 'login_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(64), unique=True, nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)
    timeout = db.Column(db.DateTime)

    def __init__(self, user_id):
        self.user_id = user_id
        self.token = secrets.token_hex(32)
        self.timeout = datetime.utcnow() + timedelta(minutes=1)

    def update_activity(self):
        self.last_activity = datetime.utcnow()
        self.timeout = self.last_activity + timedelta(hours=1)
        db.session.commit()

    @classmethod
    def create(cls, user_id):
        record = cls(user_id)
        db.session.add(record)
        db.session.commit()
        session['login_record_token'] = record.token
        print(f"Created login record with token: {record.token}")
        return record

    @classmethod
    def get_by_token(cls, token):
        return cls.query.filter_by(token=token).first()

    

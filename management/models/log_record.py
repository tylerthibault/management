from .. import db
from datetime import datetime
from management import bcrypt

class log_record(db.Model):
    """
    Represents a log record of a user's actions.

    Columns:
        id (int, primary_key): Unique identifier of the log record.
        user_id (int, foreign_key to users.id): The user who performed the action.
        action (str): The action that was performed.
        created_at (datetime, default=datetime.utcnow): The time the log record was created.
    """
    __tablename__ = "log_records"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    org_id = db.Column(db.Integer, db.ForeignKey('orgs.id'), nullable=False)
    session_token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, data: dict):
        data['session_token'] = cls.generate_session_token(data['user_id'])
        log_record = cls(user_id=data['user_id'], org_id=data['org_id'], session_token=data['session_token'])
        db.session.add(log_record)
        db.session.commit()
        return log_record

    @classmethod
    def get_by_session_token(cls, session_token):
        return cls.query.filter_by(session_token=session_token).first()

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def get_by_org_id(cls, org_id):
        return cls.query.filter_by(org_id=org_id).first()

    @staticmethod
    def generate_session_token(user_id):
        string = user_id + str(datetime.utcnow())
        hash_string = bcrypt.generate_password_hash(string).decode('utf-8')
        return hash_string
        
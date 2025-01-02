from .. import db
from datetime import datetime

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
    action = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
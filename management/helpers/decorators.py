from flask import flash, redirect, url_for, session
from functools import wraps


from datetime import datetime, timedelta
from management.models.log_record import LogRecord

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_token = session.get('session_token')
        if not session_token:
            flash('You must be logged in to access that page.', 'error')
            return redirect(url_for('users.login'))
        
        log_record = LogRecord.get_by_session_token(session_token)
        if not log_record or datetime.utcnow() - log_record.created_at > timedelta(minutes=10):
            flash('Your session has expired. Please log in again.', 'error')
            return redirect(url_for('users.login'))
        
        return f(*args, **kwargs)
    return decorated_function

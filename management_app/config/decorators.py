from functools import wraps
from flask import session, redirect, url_for, flash
from datetime import datetime, timedelta


from management_app.models.login_record import LoginRecord

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login_record_token' not in session:
            return redirect(url_for('main.index'))
        
        print(session.get('login_record_token'))
        login_record = LoginRecord.get_by_token(session.get('login_record_token'))
        print(login_record)
        if not login_record:
            last_activity = None
            flash('You are not logged in', 'error')
            return redirect(url_for('main.index'))

        last_activity = login_record.last_activity 

        if last_activity is None or datetime.utcnow() - datetime.fromisoformat(str(last_activity)) > timedelta(minutes=app.LOGIN_TIMEOUT):
            session.clear()
            flash('Your session has expired', 'error')
            return redirect(url_for('main.index'))
        
        session['last_activity'] = datetime.utcnow().isoformat()
        return f(*args, **kwargs)
    return decorated_function

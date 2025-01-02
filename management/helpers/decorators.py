from flask import flash, redirect, url_for, session
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You must be logged in to access that page.', 'error')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function

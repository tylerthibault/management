from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from management.models.user import User
from management.helpers.decorators import login_required

users = Blueprint('users', __name__)

@users.route('/management')
def index():
    return render_template('landing.html')


@users.route('/users/create', methods=['POST'])
def create():
    data == {**request.form}

    user = User.create(data)
    flash('User created successfully!', 'success')

    return redirect(url_for('users.index'))


@users.route('/users/login', methods=['POST'])
def login():
    user = User.authenticate(request.form)

    if user:
        session['user_id'] = user.id
        session['org_id'] = user.org_id
        flash('Login successful!')
        return redirect(url_for('routes.dashboard'))
    else:
        flash('Login failed. Please try again.')
        return redirect(url_for('users.index'))

@users.route('/users/logout')
@login_required
def logout():
    del session['user_id']
    del session['org_id']
    flash('Logged out successfully.')
    return redirect(url_for('users.index'))


@users.route('/page/<page>')
def page(page):
    return render_template(f'trials/page{page}.html')  


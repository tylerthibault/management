from flask import Blueprint, jsonify, request, session, url_for, flash
from flask import render_template, redirect
from management_app.forms.user import ParentForm, ChildForm, ParentLoginForm, ChildLoginForm
from management_app.models.login_record import LoginRecord
from management_app.models.user import User
from management_app.models.parent import Parent
from management_app.models.child import Child

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def index():
    return jsonify({"message": "User blueprint is working"})

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        parent_form = ParentLoginForm()
        child_form = ChildLoginForm()
        context = {
            'parent_form': parent_form,
            'child_form': child_form
        }
        return render_template('pages/login.html', **context)
    elif request.method == 'POST':
        parent_form = ParentLoginForm(request.form)
        child_form = ChildLoginForm(request.form)

        if parent_form.validate_on_submit():
            # Handle parent login
            parent = Parent.login({**parent_form.data})
            if parent:
                parent = Parent.query.filter_by(email=parent_form.email.data).first()
                user = User.query.get(parent.users_id)
                if user and user.role == 'parent':
                    LoginRecord.create(user.id)
                    return redirect(url_for('main.dashboard'))

        elif not parent_form.validate_on_submit():
            # Handle invalid parent form submission
            flash('Invalid email or password. Please try again.', 'error')
            return redirect(url_for('user.login'))

        elif child_form.validate_on_submit():
            # Handle child login
            user = User.query.filter_by(email=child_form.email.data).first()
            if user and user.role == 'child':
                session['user_id'] = user.id
                return redirect(url_for('main.dashboard'))
        
        return redirect(url_for('user.login'))

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        parent_form = ParentForm()
        child_form = ChildForm()
        context = {
            'parent_form': parent_form,
            'child_form': child_form
        }
        return render_template('pages/register.html', **context)
    elif request.method == 'POST':
        parent_form = ParentForm(request.form)
        child_form = ChildForm(request.form)

        if parent_form.validate_on_submit():
            # Handle parent registration
            user = User.create({
                'role': 'parent',
            })
            parent = Parent.create({
                'first_name': parent_form.first_name.data,
                'last_name': parent_form.last_name.data,
                'email': parent_form.email.data,
                'password': parent_form.password.data,
                'users_id': user.id
            })
            LoginRecord.create(user.id)
            return redirect(url_for('main.dashboard'))

        elif child_form.validate_on_submit():
            # Handle child registration
            user = User.create({
                'role': 'child',
            })
            child = Child.create({
                'username': child_form.username.data,
                'pin': child_form.pin.data,
                'users_id': user.id
            })
            session['user_id'] = user.id
            return redirect(url_for('main.dashboard'))
        

@user_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.index'))

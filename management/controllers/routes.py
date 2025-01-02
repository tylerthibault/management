from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from management.helpers.decorators import login_required
from management.models.user import User

routes = Blueprint('routes', __name__)


@routes.route('/management/dashboard')
@login_required
def dashboard():
    context = {
        'all_users': User.query.filter_by(org_id=session['org_id']).all(),
    }
    return render_template('dashboard.html', **context)
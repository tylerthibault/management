from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from management.helpers.decorators import login_required

routes = Blueprint('routes', __name__)


@routes.route('/management/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
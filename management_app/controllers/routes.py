from flask import Blueprint, render_template
from management_app.config.decorators import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('landing.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard.html')
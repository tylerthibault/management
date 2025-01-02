from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.org import Org
from .. import db

orgs = Blueprint('orgs', __name__)

@orgs.route('/org/create', methods=['POST'])
def create():
    data = {**request.form}
    org = Org.create(data)
    flash('Organization created successfully!')
    return redirect(url_for('users.index'))
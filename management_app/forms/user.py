from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class ParentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=45)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=45)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=45)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=60)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ChildForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=45)])
    pin = PasswordField('PIN', validators=[DataRequired(), Length(min=4, max=10)])
    submit = SubmitField('Register')

class ParentLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=45)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChildLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=45)])
    pin = PasswordField('PIN', validators=[DataRequired(), Length(min=4, max=10)])
    submit = SubmitField('Login')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(),
        Length(max=120)
    ])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=80)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ]) 

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Password', validators=[
        DataRequired()
    ]) 
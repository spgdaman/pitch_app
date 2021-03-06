from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

class SignupForm(FlaskForm):

    first_name = StringField('First name', validators=[Required()])
    last_name = StringField('Last name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')
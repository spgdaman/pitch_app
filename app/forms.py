from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class SignupForm(FlaskForm):

    first_name = StringField('First name', validators=[Required()])
    last_name = StringField('Last name', validators=[Required()])
    email = StringField('email', validators=[Required()])
    username = StringField('username', validators=[Required()])
    password = StringField('password', validators=[Required()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    username = StringField('username', validators=[Required()])
    password = StringField('password', validators=[Required()])
    submit = SubmitField('Submit')
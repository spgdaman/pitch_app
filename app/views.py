from flask import Flask, render_template
from app import app
from .forms import SignupForm, LoginForm, PitchForm
from .models import User, Credentials, Pitch
from flask_login import login_required

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_signee = User(first_name,last_name,email,username,password)

    return render_template('signup.html',form=form)

@app.route('/user/username/new_pitch', methods=['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    if pitch_form .validate_on_submit():
        pitch = pitch_form.new_pitch.data

    return render_template('newpitch.html', pitch_form=pitch_form)
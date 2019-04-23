from flask import Flask, render_template
from app import app
from .forms import SignupForm
from .models import User

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
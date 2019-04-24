from flask import render_template, redirect,url_for
from . import auth
from .forms import LoginForm,SignupForm
from ..models import Users, Credentials
from ..import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        new_login = Credentials(username,password)

    return render_template('auth/login.html', login_form = login_form)

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        new_signee = Users(firstname = first_name,lastname = last_name,email = email,username = username,password=password)

        db.session.add(new_signee)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html',form=form)
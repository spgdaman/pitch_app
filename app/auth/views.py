from flask import render_template, redirect,url_for, flash, request
from flask_login import login_user, logout_user
from . import auth
from .forms import LoginForm,SignupForm
from ..models import Users
from ..import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        password = login_form.password.data
        user = Users.query.filter_by(username = login_form.username.data).first()
        if user is not None and user.verify_password(password):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

            flash('Invalid username or password')

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

        flash("You are now Signed Up!")
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html',form=form)
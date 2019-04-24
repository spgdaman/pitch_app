from flask import render_template
from ..forms import LoginForm
from . import auth

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        new_login = Credentials(username,password)

    return render_template('auth/login.html', login_form = login_form)

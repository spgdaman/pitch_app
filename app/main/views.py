# from app import app
from . import main
from flask import Flask, render_template, redirect, url_for, abort
from .forms import PitchForm, UpdateProfile
from ..models import Users
from flask_login import login_required
from ..import db

@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = Users.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user=user)

@main.route('/user/username/new_pitch', methods=['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    if pitch_form .validate_on_submit():
        pitch = pitch_form.new_pitch.data

    return render_template('newpitch.html', pitch_form=pitch_form)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = Users.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/updateprofile.html', form = form)
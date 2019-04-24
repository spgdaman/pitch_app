# from app import app
from . import main
from flask import Flask, render_template
from .forms import PitchForm
from ..models import Pitch
from flask_login import login_required

@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/user/username/new_pitch', methods=['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    if pitch_form .validate_on_submit():
        pitch = pitch_form.new_pitch.data

    return render_template('newpitch.html', pitch_form=pitch_form)
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    new_pitch = TextAreaField('Enter new pitch', validators=[Required()])
    submit = SubmitField('submit')
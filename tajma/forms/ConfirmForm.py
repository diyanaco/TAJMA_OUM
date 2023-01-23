from wtforms import SubmitField
from flask_wtf import FlaskForm

class ConfirmForm (FlaskForm):
    confirm = SubmitField('Yes')
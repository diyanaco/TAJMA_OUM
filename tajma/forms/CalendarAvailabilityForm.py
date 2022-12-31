from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField

class CalendarAvailabilityForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    days = RadioField(
        'days', choices=["Monday", "Tuesday", "Wednesday"], validators=[DataRequired()])
    session_start = TimeField("Start", format='%H:%M')
    session_end = TimeField("End", format='%H:%M')

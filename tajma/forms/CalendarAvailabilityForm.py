from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField


class CalendarAvailabilityForm(FlaskForm):
    days = RadioField(
        'days', choices=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], validators=[DataRequired()])
    session_start = TimeField("Start", format='%H:%M')
    session_end = TimeField("End", format='%H:%M')
    submit = SubmitField('Update')


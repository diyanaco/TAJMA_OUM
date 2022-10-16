from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from .CreateCalendarEventForm import CalendarEventForm
from .LoginForm import LoginForm
from .RegistrationForm import RegistrationForm
from .VerificationForm import VerificationForm
from .PsychometricTests import AttitudeAnswer, ElearningAnswer, LearnerAnswer, UpdateAccountForm

class ConfirmForm (FlaskForm):
    confirm = SubmitField('Yes')

class SearchForm(FlaskForm):
    selectfield = SelectField('Type', choices=[('id', 'User ID'), ('firstName', 'First Name'), ('email','Email')])
    searchfield = StringField('Search')
    search = SubmitField('Search')

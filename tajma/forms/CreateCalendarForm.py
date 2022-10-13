from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email
from tajma.models import *
from flask_login import current_user

class CalendarEventForm(FlaskForm):
    todaydate = DateField('Today Date', render_kw={'readonly': True}, format='%Y-%m-%d')
    summary = StringField('Can you give a brief summary', validators=[DataRequired()])
    description = StringField('Explain briefyly your situation')
    appointmentdate = DateField(
        'Choose your appointment date', format='%Y-%m-%d')

    slot = SelectField('Choose your slot', choices=[
        ('s1', 'Session 1 : 10am - 11am'),
        ('s2', 'Session 2 : 11am - 12pm'),
        ('s3', 'Session 3 : 1pm - 2pm'),
        ('s4', 'Session 4 : 2pm - 3pm')
    ])
    counselor = SelectField('Choose your counselor', choices=[
        ('140349df-b709-4014-b38f-107d94599898', 'Dr Ahmad Idham'),
        ('140349df-b709-4014-b38f-107d94599898', 'Prof Tajudin'),
        ('91f6da50-208d-40ad-a63d-c96814c3607b', 'Caunselor Siti Saleha'),
        ('3a12da67-6afe-4cd9-87db-5535796c3799', 'Psychiatrist Adeha')
    ])
    submit = SubmitField('Submit')

    def updateCalEvent(self):
        counselor_user : User = session.query(User).join(association_user_role_table).join(Role).filter(Role.code =="COUNSELOR", User.id == self.counselor)
        patient_user : User = current_user
        
        event = CalendarEvent()
        event.summary = self.summary
        event.description = self.description
        event.appointment_date = self.appointmentdate
        event.participants.append(patient_user)
        event.participants.append(counselor_user)
        event.slot = self.slot
        db_insert_data(event)
        return True



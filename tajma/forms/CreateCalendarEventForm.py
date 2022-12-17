from tokenize import String
import uuid
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from tajma.models import *
from flask_login import current_user
from tajma.constants import RoleConstant


class CalendarEventForm(FlaskForm):
    todaydate = DateField('Today Date', render_kw={
                          'readonly': True}, format='%Y-%m-%d')
    appointmentdate = DateField(
        'Choose your appointment date', format='%Y-%m-%d')

    slot = SelectField('Choose your slot', choices=[
        ('s1', 'Session 1 : 10am - 11am'),
        ('s2', 'Session 2 : 11am - 12pm'),
        ('s3', 'Session 3 : 1pm - 2pm'),
        ('s4', 'Session 4 : 2pm - 3pm')
    ])
    counselor = SelectField('Choose your counselor', choices=[
        ('e8f8ab35-ce89-449e-a5a6-8536c7309607', 'Hamza Fadhila')
    ])
    # summary = TextAreaField('Can you give a brief summary', validators=[
    #                       DataRequired()])
    description = TextAreaField('Explain briefly your situation')
    submit = SubmitField('Submit')

    def updateCalEvent(self):
        counselor_user: User = session.query(User).join(association_user_role_table).join(
            Role).filter(Role.code == RoleConstant.COUNSELOR, User.id == self.counselor.data).scalar()
        if current_user.is_authenticated:
            patient_user: User = current_user

        # event = CalendarEvent()
        # event.id = str(uuid.uuid4())
        # # event.summary = self.summary
        # event.description = self.description.data
        # event.appointment_date = self.appointmentdate.data
        # event.participants.append(patient_user)
        # event.participants.append(counselor_user)
        # event.slot = self.slot.data
        event = CalendarEvent(id=str(uuid.uuid4()),
                              description=self.description.data,
                              appointment_date=self.appointmentdate.data,
                            #   participants=[patient_user, counselor_user],
                              slot=self.slot.data)
        event.participants.append(patient_user)
        event.participants.append(counselor_user)
        session.add(event)
        session.commit()
        # event_user_link = association_user_calendar_event_table(
        #     id=str(uuid.uuid4()),
        #     user_id=patient_user,
        #     calendar_event_id=event.id
        # )
        # event_counselor_link = association_user_calendar_event_table(
        #     id=str(uuid.uuid4()),
        #     user_id=counselor_user,
        #     calendar_event_id=event.id
        # )
        # db_insert_data(event)
        return True

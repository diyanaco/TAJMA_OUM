from tokenize import String
import uuid
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from models import *
from flask_login import current_user
from tajma.constants import RoleConstant
from typing import List


def mapCounselor(counselors: List[User]):
    return [tuple([x.id, x.gen_salutation()])for x in counselors]


class CalendarEventForm(FlaskForm):
    # Querying from tables
    slots: Slot = session.query(Slot).all()
    counselors: User = session.query(User).join(association_user_role_table).join(
        Role).filter(Role.code == RoleConstant.COUNSELOR).all()
    # List of participants
    counselor_selected: User
    patient_selected: User

    todaydate = DateField('Today Date', render_kw={
                          'readonly': True}, format='%Y-%m-%d')
    appointmentdate = DateField(
        'Choose your appointment date', format='%Y-%m-%d')

    slot = SelectField('Choose your slot', choices=slots)
    counselor = SelectField('Choose your counselor',
                            choices=mapCounselor(counselors=counselors))

    summary = TextAreaField('Can you give a brief summary', validators=[
        DataRequired()])
    # description = TextAreaField('Explain briefly your situation')
    submit = SubmitField('Submit')

    def generateTitle(self):
        return str(self.slot.data + " " + self.patient_selected)

    def updateCalEvent(self):
        self.counselor_selected: User = self.counselor.data
        # We need to authenticate the current user first, to retrieve current_user data
        if current_user.is_authenticated:
            self.patient_selected: User = current_user

        # event = CalendarEvent()
        # event.id = str(uuid.uuid4())
        # # event.summary = self.summary
        # event.description = self.description.data
        # event.appointment_date = self.appointmentdate.data
        # event.participants.append(patient_selected)
        # event.participants.append(counselor_selected)
        # event.slot = self.slot.data
        event = CalendarEvent(id=str(uuid.uuid4()),
                              title=self.generateTitle(),
                              summary=self.summary.data,
                              appointment_date=self.appointmentdate.data,
                              #   participants=[patient_selected, counselor_selected],
                              slot=self.slot.data)
        event.participants.append(self.patient_selected)
        event.participants.append(self.counselor_selected)
        session.add(event)
        session.commit()
        # event_user_link = association_user_calendar_event_table(
        #     id=str(uuid.uuid4()),
        #     user_id=patient_selected,
        #     calendar_event_id=event.id
        # )
        # event_counselor_link = association_user_calendar_event_table(
        #     id=str(uuid.uuid4()),
        #     user_id=counselor_selected,
        #     calendar_event_id=event.id
        # )
        # db_insert_data(event)
        return True

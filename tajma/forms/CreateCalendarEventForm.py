from tokenize import String
import uuid
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from models import *
from flask_login import current_user
from tajma.constants import RoleEnum
from typing import List


def mapCounselor(counselors: List[User]):
    return [tuple([x.id, x.gen_salutation()])for x in counselors]


class CalendarEventForm(FlaskForm):
    # Querying from tables
    slots = session.query(Slot).all()
    counselors = session.query(User).join(association_user_role_table).join(
        Role).filter(Role.code == RoleEnum.COUNSELOR.value).all()
    # List of participants
    counselor_selected: User
    patient_selected: User

    counselor = SelectField('Choose your counselor',
                            choices=mapCounselor(counselors=counselors))
    todaydate = DateField('Today Date', render_kw={
                          'readonly': True}, format='%Y-%m-%d')
    appointmentdate = DateField(
        'Choose your appointment date', format='%Y-%m-%d')


    summary = TextAreaField('Can you give a brief summary', validators=[
        DataRequired()])
    submit = SubmitField('Submit')

    def updateCalEvent(self):
        for c in self.counselors:
            c: User
            if c.id == self.counselor.data:
                self.counselor_selected: User = c
                break
        # We need to authenticate the current user first, to retrieve current_user data
        if current_user.is_authenticated:
            self.patient_selected: User = current_user
        event = CalendarEvent(id=str(uuid.uuid4()),
                              title=self.generateTitle(),
                              summary=self.summary.data,
                              appointment_date=self.appointmentdate.data,
                              #   participants=[patient_selected, counselor_selected],
                              #   slot=self.slot.data)
                              )
        event.participants.append(self.patient_selected)
        event.participants.append(self.counselor_selected)
        session.add(event)
        session.commit()
        return True

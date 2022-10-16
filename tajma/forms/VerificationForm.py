from tajma.models import session, Student
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm

class VerificationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    verify = SubmitField('Verify')

    def check_email(self):
        try : 
            # print(f'self.email.data : {self.email.data}')
            # userQuery = session.query(Student).filter(Student.email == self.email.data).all()
            # print(f'userQuery is : {userQuery}')
            # user = session.query(User).filter(User.email == self.email.data).scalar()
            # print(f'user is : {user}')
            if session.query(Student).filter(Student.email == self.email.data).all():
                return True
            else:
                return False
        except Exception as e :
            session.rollback()
            session.close()
            return None
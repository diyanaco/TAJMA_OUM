from flask import flash, session
from tajma import app, bcrypt
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tajma.models import User, Student, db_insert_data
from flask_login import login_user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def check_credentialsLOGIN(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user and bcrypt.check_password_hash(user.password, self.password.data):
            login_user(user, remember=False)
            return True
        else:
            return False

    def check_registered(self):
        if User.query.filter_by(email=self.email.data).first():
            return True
        else:
            return False

class VerificationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    verify = SubmitField('Verify')

    def check_email(self):
        if Student.query.filter_by(email=self.email.data).first():
            return True
        else:
            return False


class RegistrationForm(FlaskForm):
    userName = StringField("Username")
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    register = SubmitField('Register')

    # retrieve student info to import inside User table
    @staticmethod
    def retrieve_data():
        fn = Student.query.filter_by(email=session.get("email")).first()
        return(fn.firstName, fn.lastName, )

    #check insert
    def check_credentials(self):
        # if User.query.filter_by(userName=self.userName.data).first():
        #     raise ValidationError("Username already taken")
        #     return False
        # else:
        #if username not taken, then insert data
        hashed_password = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
        x, y = self.retrieve_data()
        #ISSUE 2 increment the username
        user = User(userID='04', firstName=x, lastName=y,email=self.email.data, password=hashed_password)
        db_insert_data(user)
        #Add user to session
        login_user(user)
        return True

class UpdateAccountForm(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    update = SubmitField('Update')


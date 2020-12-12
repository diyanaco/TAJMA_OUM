from flask import flash, session
from tajma import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from tajma.models import User, Student

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def check(self):
        for u in User.query.all() :
            if self.email.data == u.email:
                return True
            else :
                return False 

class VerificationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    verify = SubmitField('Verify')

    def check(self):
        #student = Student.query.filter_by(Student.data).first()
        for u in Student.query.all() :
            #check if email inside Student table
            if self.email.data == u.email:
                flash("We found your email")
                return True
        flash("Email not found")   
        return False  
        
class RegistrationForm(FlaskForm):
    userID = StringField(" User ID")
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    register = SubmitField('Register')

    #retrieve student info to import inside User table
    def retrieve_data(self):
        fn = Student.query.filter_by(email = session.get("email")).first()
        return(fn.firstName, fn.lastName)

    def check(self):
        #student = Student.query.filter_by(Student.data).first()
        for u in Student.query.all() :
            #check if email inside Student table
            if self.email.data == u.email:
                flash("We found your email")
                hashed_password = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
                x,y = self.retrieve_data(self)
                User = User(userId='01', firstName=x, lastName=y, email = self.email.data, password= hashed_password)
                return True
        flash("Email not found")   
        return False  
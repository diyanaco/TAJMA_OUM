from flask import flash
from tajma import bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from tajma.models import Student, User
from wtforms.validators import DataRequired, Email

class VerificationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    register = SubmitField('Register')

    def check(self):
        #student = Student.query.filter_by(Student.data).first()
        for u in Student.query.all() :
            #check if email inside Student table
            if self.email.data == u.email:
                flash("We found your email")
             return True
        flash("Email not found")   
        return False         
           
        
        
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from tajma.models import User
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    register = SubmitField('Register')

    def check(self):
        for u in User.query.all() :
            if self.email.data == u.email:
                flash("We found your email")
                return True
            else :
                flash("Email not found")   
                return False         
           
        
        
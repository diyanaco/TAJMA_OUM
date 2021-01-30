from flask import flash, session
from wtforms.fields.core import FieldList, FormField
from wtforms.form import Form
from tajma import app, bcrypt
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from tajma.models import Role, User, Student, db_insert_data
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
    

    def check_role(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user.roles:
            return user.roles[0].name
        else :
            return "normal"
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
        return(fn.firstName, fn.lastName, fn.gender, fn.age, fn.IC, fn.race, fn.mobile )

    #check insert
    def check_credentials(self):
        # if User.query.filter_by(userName=self.userName.data).first():
        #     raise ValidationError("Username already taken")
        #     return False
        # else:
        #if username not taken, then insert data
        hashed_password = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
        a, b, c, d, e, f, g= self.retrieve_data()
        #increment the username
        topUserID = User.query.order_by(User.userID.desc()).first()
        #If first user sign up, then assign UserID 1
        if topUserID is None:
            user = User(userID=1, firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
            db_insert_data(user)
        #Else increment the userID by 1
        else :
            user = User(userID=(topUserID.userID + 1), firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
            db_insert_data(user)
        #Add user to session
        login_user(user)
        return True

    def assign_admin(self):
        user = User.query.filter_by(email=self.email.data).first()
        user.roles.append(Role(name="Admin"))
        db_insert_data(user)

class UpdateAccountForm(FlaskForm):
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    update = SubmitField('Update')

class Elearning(FlaskForm):
    #trait 1 Kemahiran Belajar
    answer1 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer2 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer3 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer4 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer5 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer6 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer7 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer8 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer9 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])

    #trait 2 Kemahiran Literasi
    answer10 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer11 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer12 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer13 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer14 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer15 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer16 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer17 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer18 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer19 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer20 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer21 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])

    #trait 3 Kemahiran Hidup

    submit = SubmitField("Submit")


class AnswerElearningTrait1Form(FlaskForm):
    answer1 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer2 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    submit = SubmitField("Submit")
    desc = "Kemahiran Belajar"

class AnswerElearningTrait2Form(FlaskForm):
    answer1 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer2 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    submit = SubmitField("Submit")
    desc = "Kemahiran Literasi"

class AnswerElearningTrait3Form(FlaskForm):
    answer1 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    answer2 = RadioField('', choices=[(1,'One'),(2,'two'),(3,'Three'),(4,'Four'),(5,'Five')])
    submit = SubmitField("Submit")
    desc = "Kemahiran Hidup"







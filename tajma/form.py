from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import login_user
from models import *
from tajma import bcrypt
from flask import session as localSession, current_app
import uuid
from sqlalchemy import insert
from flask_principal import identity_changed, Identity

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')

#     def check_login(self):
#         try :
#             print(f'email data is : {self.email.data}')
#             # session.rollback()
#             # session.close()
#             user = session.query(User).filter(User.email == self.email.data).scalar()
#             print(f'user is : {user}')
#             if user and bcrypt.check_password_hash(user.password, self.password.data):
#                 role_code = self.check_role(user)
#                 login_user(user, remember=False)
#                 identity_changed.send(current_app._get_current_object(),
#                             identity=Identity(user.id))
#                 return True
#             else:
#                 return False
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None
    

#     def check_role(self, user : User):
#         try :
#             role = session.query(Role).join(association_user_role_table).join(User).filter(association_user_role_table.columns.user_id == user.id).scalar()
#             print(f'role is : {role}')
#             if role:
#                 return role.code
#             else :
#                 return "NORMAL"
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None
    
#     def check_registered(self):
#         try :
#             if session.query(User).filter(User.email == self.email.data).scalar():
#                 return True
#             else:
#                 return False

#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None

# class VerificationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     verify = SubmitField('Verify')

#     def check_email(self):
#         try : 
#             # print(f'self.email.data : {self.email.data}')
#             # userQuery = session.query(Student).filter(Student.email == self.email.data).all()
#             # print(f'userQuery is : {userQuery}')
#             # user = session.query(User).filter(User.email == self.email.data).scalar()
#             # print(f'user is : {user}')
#             if session.query(Student).filter(Student.email == self.email.data).all():
#                 return True
#             else:
#                 return False
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None

# class RegistrationForm(FlaskForm):
#     userName = StringField("Username")
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     firstName = StringField('First Name')
#     lastName = StringField('Last Name')
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     register = SubmitField('Register')

#     # retrieve student info to import inside User table
#     @staticmethod
#     def retrieve_data():
#         try : 
#             fn = session.query(Student).filter(Student.email == localSession.get("email")).scalar()
#             # fn = Student.query.filter_by(email=session.get("email")).first()
#             return(fn.firstName, fn.lastName, fn.gender, fn.age, fn.IC, fn.race, fn.mobile )
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None

#     #check insert
#     def check_credentials(self):
#         try : 
#             # if User.query.filter_by(userName=self.userName.data).first():
#             #     raise ValidationError("Username already taken")
#             #     return False
#             # else:
#             #if username not taken, then insert data
#             hashed_password = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
#             a, b, c, d, e, f, g= self.retrieve_data()
#             #increment the username
#             # topUserID = User.query.order_by(User.desc()).first()
#             # topUserID = session.query(User).order_by(User.desc()).first()
#             user = User(id= str(uuid.uuid4()), firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
#             db_insert_data(user)
#             # userRole = association_user_role_table()
#             normal_role = session.query(Role).filter(Role.name == "NORMAL").scalar()
#             normal_role_id = session.query(Role).filter(Role.name == "NORMAL").scalar().id
#             print(f'normal role is {normal_role}')
#             print(f'normal role id is {normal_role_id}')
            
#             #Insert into link table:
#             stmt = insert(association_user_role_table).values(id=str(uuid.uuid4()), user_id=user.id, role_id=normal_role_id)
#             with engine.connect() as conn:
#                 result = conn.execute(stmt)
#                 # conn.commit()
#             print(f'inserted primary key : {result.inserted_primary_key}')
#             # userRole = UserRoleLink(id=str(uuid.uuid4()), user_id=user.id, role_id=normal_role_id)
#             # print(f'userRole is : {userRole}')
#             # db_insert_data(user)
#             #If first user sign up, then assign UserID 1
#             # if topUserID is None:
#             #     user = User(id=1, firstName=a, lastName=b,email=self.self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
#             #     db_insert_data(user)
#             # #Else increment the userID by 1
#             # else :
#             #     user = User(id=(topUserID.id + '1'), firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
#             #     db_insert_data(user)
#             # #Add user to session
#             login_user(user)
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None
#         return True

#     def assign_admin(self):
#         try : 
#             user = User.query.filter_by(email=self.self.email.data).first()
#             user.roles.append(Role(name="Admin"))
#             db_insert_data(user)
#         except Exception as e :
#             session.rollback()
#             session.close()
#             return None

# class UpdateAccountForm(FlaskForm):
#     picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
#     #email = StringField('Email', validators=[DataRequired(), Email()])
#     update = SubmitField('Update')

#WTF Form doesnt cater for input required for radio field. THis code bypass it.
# class FieldsRequiredForm(FlaskForm):
#     """Require all fields to have content. This works around the bug that WTForms radio
#     fields don't honor the `DataRequired` or `InputRequired` validators.
#     """

#     class Meta:
#         def render_field(self, field, render_kw):
#             render_kw.setdefault('required', True)
#             return super().render_field(field, render_kw)

# class ElearningAnswer(FieldsRequiredForm):
#     #trait 1 Kemahiran Belajar
#     answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer8 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer9 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

#     #trait 2 Kemahiran Literasi
#     answer10 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer11 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer12 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer13 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer14 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer15 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer16 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer17 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer18 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer19 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer20 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer21 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

#     #trait 3 Kemahiran Hidup
#     answer22 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer23 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer24 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer25 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer26 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer27 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer28 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer29 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer30 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)



#     submit = SubmitField("Submit")

# class AttitudeAnswer(FieldsRequiredForm):
#     #trait 1 Motivasi
#     answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

#     #trait 2 Keterbukaan
#     answer8 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer9 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer10 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer11 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer12 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer13 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer14 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer15 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

#     #trait 3 Kestabilan emosi
#     answer16 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer17 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer18 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer19 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer20 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer21 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer22 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)

#     # #Trait 4 Keberkesanan Diri
#     # answer23 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     # answer24 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer25 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer26 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer27 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer28 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer29 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
    
#     # #Trait 5 Kebolehsuaian
#     # answer30 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer31 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer32 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer33 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer34 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer35 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer36 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer37 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

#     # #Akauntabiliti/Kebertanggungjawab
#     # answer38 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer39 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer40 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer41 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer42 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer43 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer44 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

#     # #Pengarahan diri
#     # answer45 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer46 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer47 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer48 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer49 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer50 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

#     # #Silang budaya
#     # answer51 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer52 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer53 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer54 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer55 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer56 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer57 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer58 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

#     # #Daya ketahanan
#     # answer59 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer60 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer61 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer62 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer63 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer64 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer65 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])
#     # answer66 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')])

#     submit = SubmitField("Submit")

# class LearnerAnswer(FieldsRequiredForm):
#     #trait 1 
#     answer1 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer2 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer3 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer4 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer5 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer6 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     answer7 = RadioField('', choices=[(1,'One'),(2,'Two'),(3,'Three'),(4,'Four'),(5,'Five')], default=1)
#     submit = SubmitField("Submit")

class ConfirmForm (FlaskForm):
    confirm = SubmitField('Yes')

class SearchForm(FlaskForm):
    selectfield = SelectField('Type', choices=[('id', 'User ID'), ('firstName', 'First Name'), ('email','Email')])
    searchfield = StringField('Search')
    search = SubmitField('Search')




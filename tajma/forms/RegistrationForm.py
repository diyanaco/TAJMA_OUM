from flask import session as localSession
from tajma import bcrypt
from flask_wtf import FlaskForm
from models import session, Student, User, db_insert_data, Role, association_user_role_table, engine
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from sqlalchemy import insert
from flask_login import login_user
import uuid
from tajma import user_datastore
from tajma.constants import RoleEnum


class RegistrationForm(FlaskForm):
    userName = StringField("Username")
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    firstName = StringField('First Name')
    lastName = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    register = SubmitField('Register')

    # retrieve student info to import inside User table
    @staticmethod
    def retrieve_data():
        try:
            fn = session.query(Student).filter(
                Student.email == localSession.get("email")).scalar()
            # fn = Student.query.filter_by(email=session.get("email")).first()
            return(fn.firstName, fn.lastName, fn.gender, fn.age, fn.IC, fn.race, fn.mobile)
        except Exception as e:
            session.rollback()
            session.close()
            return None

    # check insert
    def check_credentials(self):
        try:
            # if User.query.filter_by(userName=self.userName.data).first():
            #     raise ValidationError("Username already taken")
            #     return False
            # else:
            # if username not taken, then insert data
            hashed_password = bcrypt.generate_password_hash(
                self.password.data).decode('utf-8')
            a, b, c, d, e, f, g = self.retrieve_data()
            # increment the username
            # topUserID = User.query.order_by(User.desc()).first()
            # topUserID = session.query(User).order_by(User.desc()).first()
            # user = User(id= str(uuid.uuid4()), firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
            # Login user after su
            user = user_datastore.create_user(
                id=str(uuid.uuid4()), email=self.email.data, password=hashed_password)
            session.commit()
            # db_insert_data(user)
            # userRole = association_user_role_table()
            normal_role = session.query(Role).filter(
                Role.code == RoleEnum.STUDENT).scalar()
            normal_role_id = session.query(Role).filter(
                Role.code == RoleEnum.STUDENT).scalar().id
            print(f'normal role is {normal_role}')
            print(f'normal role id is {normal_role_id}')

            # Insert into link table:
            stmt = insert(association_user_role_table).values(
                id=str(uuid.uuid4()), user_id=user.id, role_id=normal_role_id)
            with engine.connect() as conn:
                result = conn.execute(stmt)
                # conn.commit()
            print(f'inserted primary key : {result.inserted_primary_key}')
            # userRole = UserRoleLink(id=str(uuid.uuid4()), user_id=user.id, role_id=normal_role_id)
            # print(f'userRole is : {userRole}')
            # db_insert_data(user)
            # If first user sign up, then assign UserID 1
            # if topUserID is None:
            #     user = User(id=1, firstName=a, lastName=b,email=self.self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
            #     db_insert_data(user)
            # #Else increment the userID by 1
            # else :
            #     user = User(id=(topUserID.id + '1'), firstName=a, lastName=b,email=self.email.data, password=hashed_password, gender=c, age=d, IC=e, race=f, mobile=g)
            #     db_insert_data(user)
            # #Add user to session
            login_user(user)
        except Exception as e:
            session.rollback()
            session.close()
            return None
        return True

    def assign_admin(self):
        try:
            user = User.query.filter_by(email=self.self.email.data).first()
            user.roles.append(Role(name="Admin"))
            db_insert_data(user)
        except Exception as e:
            session.rollback()
            session.close()
            return None

from tajma import bcrypt
from models import session, User, Role, association_user_role_table
from flask import current_app
from flask_wtf import FlaskForm
from flask_security import login_user, current_user
from flask_principal import identity_changed, Identity
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def check_login(self):
        try :
            user = session.query(User).filter(User.email == self.email.data).scalar()
            if user and bcrypt.check_password_hash(user.password, self.password.data):
                role_codes = self.check_role(user)
                is_login = login_user(user, remember=False)
                identity_changed.send(current_app._get_current_object(),
                            identity=Identity(user.id))
                return True
            else:
                return False
        except Exception as e :
            session.rollback()
            session.close()
            return None
    

    def check_role(self, user : User):
        try :
            roles = session.query(Role).join(association_user_role_table).join(User).filter(association_user_role_table.columns.user_id == user.id).all()
            if roles:
                return [x for x in roles if x.code]
            else :
                return "NORMAL"
        except Exception as e :
            session.rollback()
            session.close()
            return None
    
    def check_registered(self):
        try :
            if session.query(User).filter(User.email == self.email.data).scalar():
                return True
            else:
                return False

        except Exception as e :
            session.rollback()
            session.close()
            return None

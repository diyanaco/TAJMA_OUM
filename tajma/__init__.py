
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_user import UserManager
from flask_babelex import Babel

class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = '1d66b518598641b6d88a3f0115780daf hello cookoo budak baik h e u a j dasdasdj'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tajma.db'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
babel = Babel(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# the category for error login message
login_manager.login_message_catagory = 'info'

from tajma import routes
from tajma.models import User

user_manager = UserManager(app, db, User)



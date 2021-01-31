
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d66b518598641b6d88a3f0115780daf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tajma.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# the category for error login message
login_manager.login_message_catagory = 'info'

from tajma import routes
from tajma.models import User




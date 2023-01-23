import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_principal import Principal
from dotenv import load_dotenv
from flask_security import SQLAlchemySessionUserDatastore, Security
from models import session, User, Role

app = Flask(__name__)
principals = Principal(app)
bcrypt = Bcrypt(app)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

user_datastore = SQLAlchemySessionUserDatastore(session,
                                                User, Role)
security = Security(app, user_datastore)

load_dotenv()
from . import  routes
# load default configuration
app.config.from_object('tajma.settings')
# load environment configuration
##This below is not working, need to find a way to get user enviroment variables
if 'OUMPSY_SETTINGS' in os.environ:
    app.config.from_envvar('OUMPSY_SETTINGS')
# load app specified configuration
app.config.update({'APP_PATH': app.root_path})
with app.app_context():
    routes.init_app(app)
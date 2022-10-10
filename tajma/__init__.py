import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_principal import Principal
from dotenv import load_dotenv

app = Flask(__name__)
principals = Principal(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

load_dotenv()
from . import  routes, services, models
# load default configuration
app.config.from_object('tajma.settings')
# load environment configuration
##This below is not working, need to find a way to get user enviroment variables
if 'OUMPSY_SETTINGS' in os.environ:
    app.config.from_envvar('OUMPSY_SETTINGS')
# load app sepcified configuration
app.config.update({'APP_PATH': app.root_path})
print(f'app config is : {app.config}')
#If theres initial config to create app, upon instantiate the app
# if config is not None:
#     if isinstance(config, dict):
#         app.config.update(config)
#     elif config.endswith('.py'):
#         app.config.from_pyfile(config)
#with app.app_context():
routes.init_app(app)
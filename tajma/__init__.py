from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager
import os
from dotenv import load_dotenv

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

def create_app(config=None):
    load_dotenv()
    from . import  routes, services
    # load default configuration
    app.config.from_object('tajma.settings')
    # load environment configuration
    # if 'PSYCHOMETRIC_CONFIG_FLASK' in os.getenv:
    #     app.config.from_envvar('PSYCHOMETRIC_CONFIG_FLASK')
    # load app sepcified configuration
    app.config.update({'APP_PATH': app.root_path})
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    routes.init_app(app)
    # services.init_app(app)
    return app
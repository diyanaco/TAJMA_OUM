
import imp
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '1d66b518598641b6d88a3f0115780daf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tajma.db'
#increase timeout in case database locked
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {
        'timeout': 15
    }
}
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# the category for error login message
login_manager.login_message_catagory = 'info'

#SqlAlchemy
db_url = os.getenv('DATABASE_OUM_URL')
print(db_url)
engine = create_engine(db_url, echo=True)
Base = declarative_base()
print(f'base metada is : {Base.metadata}')

#another test

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Base.metadata.drop_all(engine)

# from tajma.models import User, Role, UserRoles, Student, Question, Elearning, Learner, Attitude, Code
from tajma.models.AttitudeModel import Attitude
from tajma.models.ClientSidePermissionModel import ClientSidePermisssion 
from tajma.models.ElearningModel import Elearning
from tajma.models.LearnerModel import Learner
from tajma.models.QuestionModel import Question
from tajma.models.RoleModel import Role
from tajma.models.StudentModel import Student
from tajma.models.UserModel import User
from tajma.models.UserRoleLinkModel import association_user_role_table
# from tajma.model.UserRoleLinkModel import UserRoles

Base.metadata.create_all(engine)

from tajma import routes
# from tajma.models import User

# # Only applicable to sqlite to prevent error
# with app.app_context():
#     if db.engine.url.drivername == 'sqlite':
#         migrate.init_app(app, db, render_as_batch=True)
#     else:
#         migrate.init_app(app, db)




from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from tajma import login_manager
import os

db_url = os.getenv('DATABASE_OUM_URL')
engine = create_engine(db_url, echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()

from .AttitudeModel import Attitude
from .LearnerModel import Learner
from .ElearningModel import Elearning
from .UserModel import User
from .ClientSidePermissionModel import ClientSidePermisssion
from .QuestionModel import Question
from .RoleModel import Role
from .StudentModel import Student
from .UserRoleLinkModel import association_user_role_table

Base.metadata.create_all(engine)
# db.drop_all()

@login_manager.user_loader
def load_user(user_id):
    print(f'user is : {session.query(User).get(user_id)}')
    return session.query(User).get(user_id)

def db_insert_data(model):
    session.add(model)
    session.commit()

def db_update_data():
    session.commit()
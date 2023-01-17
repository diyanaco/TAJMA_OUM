from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from tajma import login_manager
import os
from sqlalchemy.ext.declarative import declarative_base

db_url='mysql://zaim:zaim@localhost:3306/oumpsy'
# db_url='sqlite:///oumpsy.db'
# db_url = "sqlite:///tajma.db"
# db_url = os.getenv('DATABASE_OUM_URL_SQLITE')
# print("db from env", db_url)
# check_same_thread
# err : sqlite objects created in a thread can only be used in that same thread sqlalchemy
#For sqlite
# engine = create_engine(db_url,connect_args={"check_same_thread": False}, echo=True)
engine = create_engine(db_url, echo=True, pool_size=10, max_overflow=20)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
# Session = sessionmaker()
# Session.configure(bind=engine)
# session = Session()
Base = declarative_base()
Base.query = session.query_property()

from .AttitudeModel import Attitude
from .LearnerModel import Learner
from .ElearningModel import Elearning
from .UserModel import User
from .ClientSidePermissionModel import ClientSidePermisssion
from .QuestionModel import Question
from .RoleModel import Role
from .StudentModel import Student
# from .CalendarEventModel import CalendarEvent
from .UserRoleLinkModel import association_user_role_table
from .CalendarEventModel import CalendarEvent
from .UserCalendarEventModel import association_user_calendar_event_table
from .SlotModel import Slot

Base.metadata.create_all(engine)
# db.drop_all()

# @login_manager.user_loader
# def load_user(user_id):
#     print(f'user is : {session.query(User).get(user_id)}')
#     return session.query(User).get(user_id)

def db_insert_data(model):
    try :
        session.add(model)
        session.commit()
    except Exception as e :
        session.rollback()
        session.close()
        print(str(e))


def db_update_data():
    try :
        session.commit()
    except Exception as e :
        session.rollback()
        session.close()
        print(str(e))
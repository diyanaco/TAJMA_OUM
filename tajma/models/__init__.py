from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from tajma import login_manager
import os

# db_url = os.getenv('DATABASE_OUM_URL')
db_url = "sqlite:///tajma.db"
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
# from .CalendarEventModel import CalendarEvent
from .UserRoleLinkModel import association_user_role_table
from .CalendarEventModel import CalendarEvent
from .UserCalendarEventModel import association_user_calendar_event_table

Base.metadata.create_all(engine)
# db.drop_all()

@login_manager.user_loader
def load_user(user_id):
    print(f'user is : {session.query(User).get(user_id)}')
    return session.query(User).get(user_id)

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
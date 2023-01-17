from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url='mysql://zaim:zaim@localhost:3306/oumpsy'
engine = create_engine(db_url, echo=True, pool_size=10, max_overflow=20)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
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
from .UserRoleLinkModel import association_user_role_table
from .CalendarEventModel import CalendarEvent
from .UserCalendarEventModel import association_user_calendar_event_table
from .SlotModel import Slot

Base.metadata.create_all(engine)

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
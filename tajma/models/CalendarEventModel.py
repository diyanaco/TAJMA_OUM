from sqlalchemy import Column, String, Integer, ForeignKey
from . import Base

class CalendarEvent(Base):
    __tablename__ = "psy_calendar_event"
    id = Column('id', Integer, primary_key=True, nullable=False)
    event = Column('event', String(50))
    description = Column('description', String(100))
    userID = Column(String(50), ForeignKey('psy_user.id'), nullable=True)

    def __repr__(self):
        return f"CalendarEvent('{self.id}', '{self.event}', {self.description}, {self.userID})"

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .UserCalendarEventModel import association_user_calendar_event_table
from . import Base
class CalendarEvent(Base):
    __tablename__ = "psy_calendar_event"
    id = Column('id', String(50), primary_key=True, nullable=False)
    summary = Column('summary', String(200))
    # description = Column('description', String(500))
    appointment_date = Column('appointment_date', DateTime)
    slot = Column("slot", String(50))
    title = Column("title", String(50))

    participants = relationship("User", secondary=association_user_calendar_event_table)

    def __repr__(self):
        return f"CalendarEvent('{self.id}', {self.description}, {self.participants})"

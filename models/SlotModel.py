from sqlalchemy import Column, String, DateTime, Integer, Float, Time, ForeignKey
from . import Base


class Slot(Base):
    __tablename__ = "psy_slot"

    def __init__(self, id, start_slot, end_slot, days):
        self.id = id
        self.start_slot = start_slot
        self.end_slot = end_slot
        self.days = days

    id = Column(String(50), primary_key=True)
    # If end slot is emptied, it means a one time meeting,
    # else it will be a recurring meeting
    start_slot = Column("start_slot", Time)
    end_slot = Column("end_slot", Time)
    hours = Column("hours", Float)
    counselor_id = Column("counselor_id",String(50), ForeignKey("psy_user.id"))
    days = Column(String(50))

    # AVAILABILITY
    # BREAK
    # SESSION
    # BREAK_BETWEEN_SESSION
    type = Column(String(50))

    def __repr__(self):
        return f"Slot('{self.id}', '{self.start_slot}', {self.end_slot})"

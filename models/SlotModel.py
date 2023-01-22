from sqlalchemy import Column, String, DateTime, Integer, Float, Time
from . import Base


class Slot(Base):
    __tablename__ = "psy_slot"

    def __init__(self, id, start_slot, end_slot):
        self.id = id
        self.start_slot = start_slot
        self.end_slot = end_slot

    id = Column(String(50), primary_key=True)
    # If end slot is emptied, it means a one time meeting,
    # else it will be a recurring meeting
    start_slot = Column("start_slot", Time)
    end_slot = Column("end_slot", Time)
    hours = Column("hours", Float)
    # AVAILABILITY
    # BREAK
    # SESSION
    # BREAK_BETWEEN_SESSION
    type = Column(String(50))

    def __repr__(self):
        return f"Slot('{self.id}', '{self.start_slot}', {self.end_slot})"

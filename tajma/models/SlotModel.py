# import imp
from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy.orm import relationship
from .UserRoleLinkModel import association_user_role_table
from . import Base

class Slot(Base):
    __tablename__="psy_slot"
    id = Column(String(50), primary_key=True)
    # name = Column(String(50), unique=True)
    # code = Column(String(50))
    start_slot = Column("start_slot", DateTime)
    end_slot = Column("end_slot", DateTime)
    hours = Column("hours", Float)
    # AVAILABILITY
    # BREAK
    # SESSION
    # BREAK_BETWEEN_SESSION 
    type = Column(String(50))


    # user_id = relationship('User', secondary=association_user_role_table)
    def __repr__(self):
        return f"Slot('{self.id}', '{self.start_slot}', {self.end_slot})"


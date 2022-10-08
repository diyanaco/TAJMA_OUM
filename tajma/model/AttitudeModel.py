from tajma import Base
from sqlalchemy import Column, String, Float

class Attitude(Base):
    __tablename__ = "psy_attitude"
    id = Column(String(50),primary_key=True, nullable=False)
    #motivasi
    mt =Column(Float, nullable=True)
    #keterbukaan
    kt =Column(Float, nullable=True)
    #kestabilan emosi
    ke =Column(Float, nullable=True)
    
    userID = Column(String(50), nullable=True)
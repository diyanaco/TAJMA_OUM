from sqlalchemy import Column, String, Float
from . import Base
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

    def __repr__(self):
        return f"Attitude('{self.mt}', '{self.kt}', {self.ke}, {self.id})"
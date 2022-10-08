from tajma import Base 
from sqlalchemy import Column, String, Float

class Elearning(Base):
    __tablename__ = "psy_elearning"
    id = Column(String(50),primary_key=True, nullable=False)
    #kemahiran belajar
    kb =Column(Float, nullable=True)
    #kemahiran literasi
    kl =Column(Float, nullable=True)
    #kemahiran hidup
    kh =Column(Float, nullable=True)
    userID = Column(String(50), nullable=True)
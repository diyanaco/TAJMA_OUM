from sqlalchemy import Column, String, Float
from . import Base
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
    
    def __repr__(self):
        return f"Elearning('{self.kb}', '{self.kl}','{self.kh}', {self.id})"
from tajma import Base
from sqlalchemy import Column, String, Float

class Learner(Base):
    __tablename__ = "psy_learner"
    id = Column(String(50), primary_key=True, nullable=False)
    tr1 =Column(Float, nullable=True)
    userID = Column(String(50), nullable=True)
    
    def __repr__(self):
        return f"Learner('{self.tr1}', '{self.userID}', {self.id})"
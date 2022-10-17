from sqlalchemy import Column, String
from . import Base
class Question(Base):
    __tablename__ = "psy_question"
    id = Column(String(50), primary_key=True, nullable=False)
    code = Column(String(50))
    question = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Question('{self.question}', '{self.code}')"
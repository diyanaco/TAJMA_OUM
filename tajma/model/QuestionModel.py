from tajma import Base
from sqlalchemy import Column, String

class Question(Base):
    __tablename__ = "psy_question"
    instruCode = Column(String(50), primary_key=True)
    question = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Question('{self.question}', '{self.instruCode}')"
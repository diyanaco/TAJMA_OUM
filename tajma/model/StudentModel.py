from tajma import Base
from sqlalchemy import Column, String

class Student(Base):
    __tablename__ = "psy_student"
    studentID = Column(String(50), primary_key=True)
    firstName = Column(String(50), nullable=True)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    profPic = Column(String(50), nullable=False, default='default.jpg')
    gender = Column(String(50), nullable=False)
    age = Column(String(50), nullable=False)
    IC = Column(String(50), nullable=False)
    race = Column(String(50), nullable=False)
    mobile = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Student('{self.email}', '{self.firstName}')"
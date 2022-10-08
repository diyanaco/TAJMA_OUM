from tajma import Base
from sqlalchemy import Column, String

class Code(Base):
    __tablename__ = "psy_code"
    id = Column(String(50),primary_key=True, nullable=False)
    code = Column(String(50), nullable=False, primary_key=True)
    desc = Column(String(50), nullable=False)
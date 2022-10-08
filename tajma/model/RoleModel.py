from tajma import Base
from sqlalchemy import Column, String

class Role(Base):
    __tablename__="psy_role"
    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
from tajma import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from tajma.model.UserRoleLinkModel import association_user_role_table
class Role(Base):
    __tablename__="psy_role"
    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
    user_id = relationship('UserModel', secondary=association_user_role_table)

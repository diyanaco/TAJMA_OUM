from tajma import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from tajma.model.UserRoleLinkModel import association_user_role_table
class Role(Base):
    __tablename__="psy_role"
    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
    code = Column(String(50))
    user_id = relationship('User', secondary=association_user_role_table)
    
    def __repr__(self):
        return f"Role('{self.name}', '{self.code}', {self.id})"


# import imp
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .UserRoleLinkModel import association_user_role_table
from . import Base
from flask_security import RoleMixin

class Role(Base, RoleMixin):
    __tablename__="psy_role"
    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
    code = Column(String(50))
    user_id = relationship('User', secondary=association_user_role_table)
    
    def __repr__(self):
        return f"Role('{self.name}', '{self.code}', {self.id})"


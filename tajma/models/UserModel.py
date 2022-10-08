from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from .UserRoleLinkModel import association_user_role_table
from . import Base

class User(Base, UserMixin):
    __tablename__ = "psy_user"
    id = Column(String(50), primary_key=True)
    firstName = Column(String(50), nullable=True)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    gender = Column(String(50), nullable=False)
    age = Column(String(50), nullable=False)
    profPic = Column(String(50), nullable=False, default='default.jpg')
    IC = Column(String(50), nullable=False)
    race = Column(String(50), nullable=False)
    mobile = Column(String(50), nullable=False)
    # roles = relationship('Role', secondary='psy_user_roles')
    # active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email_confirmed_at = Column(DateTime)
    elearningTaken = Column(Boolean, nullable =True)
    learnerTaken = Column(Boolean, nullable =True)
    attitudeTaken = Column(Boolean, nullable =True)

    role_id = relationship("Role", secondary=association_user_role_table)

    #override get_id method from UserMixin
    def get_id(self):
        return self.id
    def get_first_name(self):
        return self.firstName
    def get_last_name(self):
        return self.lastName
    def get_email(self):
        return self.email
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def get_profPic(self):
        return self.profPic
    def get_IC(self):
        return self.IC
    def get_race(self):
        return self.race
    def get_mobile(self):
        return self.mobile

    def __repr__(self):
        return f"User('{self.email}', '{self.password}', {self.id})"
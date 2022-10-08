from sqlalchemy import Column, String, ForeignKey, Table
from . import Base

association_user_role_table = Table(
    "psy_user_role_link",
    Base.metadata,
    Column("id",String(50), primary_key=True),
    Column("user_id", ForeignKey("psy_user.id")),
    Column("role_id", ForeignKey("psy_role.id")),
)

# class UserRoleLink(Base):
#     __tablename__ = 'psy_user_role_link'
#     id = Column(String(50), primary_key=True)
#     user_id = Column(String(50), ForeignKey("psy_user.id"))
#     role_id = Column(String(50), ForeignKey("psy_role.id"))
    
#     def __repr__(self):
#         return f"UserRoleLink('{self.user_id}', '{self.role_id}', {self.id})"
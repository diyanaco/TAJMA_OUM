from sqlalchemy import Column, String
from . import Base
class ClientSidePermisssion(Base):
    __tablename__ = "psy_client_side_permission"
    id = Column(String(50),primary_key=True, nullable=False)
    name = Column(String(50))
    code = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)

    def __repr__(self):
        return f"ClientSidePermisssion('{self.name}', '{self.code}', {self.id})"
from tajma import Base
from sqlalchemy import Column, String, ForeignKey

class UserRoles(Base):
    __tablename__ = 'psy_user_roles'
    id = Column(String(50), primary_key=True)
    user_id = Column(String(50), ForeignKey('psy_user.id', ondelete='CASCADE'))
    role_id = Column(String(50), ForeignKey('psy_role.id', ondelete='CASCADE'))
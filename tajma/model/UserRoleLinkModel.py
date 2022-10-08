from tajma import Base
from sqlalchemy import Column, String, ForeignKey, Table

association_user_role_table = Table(
    "psy_user_role_link",
    Base.metadata,
    Column("user_id", ForeignKey("psy_user.id")),
    Column("role_id", ForeignKey("psy_role.id")),
)
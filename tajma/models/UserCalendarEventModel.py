from sqlalchemy import Column, String, ForeignKey, Table
from . import Base

association_user_calendar_event_table = Table(
    "psy_user_calendar_event_link",
    Base.metadata,
    Column("id",String(50), primary_key=True),
    Column("user_id", ForeignKey("psy_user.id")),
    Column("calendar_event_id", ForeignKey("psy_calendar_event.id"), unique=True),
)
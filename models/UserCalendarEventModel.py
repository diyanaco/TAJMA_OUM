from sqlalchemy import Column, String, ForeignKey, Table
from . import Base

association_user_calendar_event_table = Table(
    "psy_user_calendar_event_link",
    Base.metadata,
    Column("user_id", ForeignKey("psy_user.id"), primary_key=True),
    Column("calendar_event_id", ForeignKey("psy_calendar_event.id"), primary_key=True)
)
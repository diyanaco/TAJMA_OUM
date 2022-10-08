"""rename table calender_event

Revision ID: 54e6517f5d16
Revises: e630c7e50001
Create Date: 2022-10-08 23:55:52.776348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '54e6517f5d16'
down_revision = 'e630c7e50001'
branch_labels = None
depends_on = None

# #Checkin must be done before creating new table
# conn = op.get_bind()
# inspector = Inspector.from_engine(conn)
# tables = inspector.get_table_names()

def upgrade():
    op.rename_table('psy_calendar_event', 'psy_calendar_events') 
    pass


def downgrade():
    op.rename_table('psy_calendar_events', 'psy_calendar_event')
    pass

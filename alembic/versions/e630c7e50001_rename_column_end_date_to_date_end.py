"""Rename column end_date to date_end

Revision ID: e630c7e50001
Revises: 8538d7c25296
Create Date: 2022-10-08 23:35:13.059704

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = 'e630c7e50001'
down_revision = '8538d7c25296'
branch_labels = None
depends_on = None

# #Get a list of columns from table
# conn = op.get_bind()
# inspector = Inspector.from_engine(conn)
# columns = inspector.get_columns('psy_calendar_event')

def upgrade():
    #for mysql, needs to put existing_type
    op.alter_column('psy_calendar_event', 'end_date', nullable=False, new_column_name='date_end', existing_type=sa.DateTime)
    pass


def downgrade():
    op.alter_column('psy_calendar_event', 'date_end', nullable=False, new_column_name='end_date', existing_type=sa.DateTime)
    pass

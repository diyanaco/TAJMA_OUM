"""Add new colum table calendar_event

Revision ID: 8538d7c25296
Revises: f76ff87c1203
Create Date: 2022-10-08 23:32:32.893868

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '8538d7c25296'
down_revision = 'f76ff87c1203'
branch_labels = None
depends_on = None

# # Get a list of columns from table
# conn = op.get_bind()
# inspector = Inspector.from_engine(conn)
# columns = inspector.get_columns('psy_calendar_event')

# added_cols = ['end_date', 'start_date']
# check = all(item in columns for item in added_cols)


def upgrade():
    op.add_column('psy_calendar_event', sa.Column('end_date', sa.DateTime))
    op.add_column('psy_calendar_event', sa.Column('start_date', sa.DateTime))
    pass

def downgrade():
    op.drop_column('psy_calendar_event', 'end_date')
    op.drop_column('psy_calendar_event', 'start_date')
    pass

"""create calendar_events table

Revision ID: f76ff87c1203
Revises: 3da17d7476c1
Create Date: 2022-10-08 23:25:12.401860

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = 'f76ff87c1203'
down_revision = '3da17d7476c1'
branch_labels = None
depends_on = None

# #Checkin must be done before creating new table
# conn = op.get_bind()
# inspector = Inspector.from_engine(conn)
# tables = inspector.get_table_names()

def upgrade():
    op.create_table(
        'psy_calendar_event',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('event', sa.String(50), nullable=False),
        sa.Column('user_id', sa.String(50), sa.ForeignKey('psy_user.id')),
        sa.Column('description', sa.String(100)),
    )
    pass

def downgrade():
    op.drop_table('psy_calendar_event')
    pass

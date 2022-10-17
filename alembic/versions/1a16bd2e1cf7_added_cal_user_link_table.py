"""Added cal user link table

Revision ID: 1a16bd2e1cf7
Revises: 54e6517f5d16
Create Date: 2022-10-13 19:54:01.898413

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1a16bd2e1cf7'
down_revision = '54e6517f5d16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('psy_calendar_event', sa.Column('summary', sa.String(length=200), nullable=True))
    op.add_column('psy_calendar_event', sa.Column('appointment_date', sa.DateTime(), nullable=True))
    op.add_column('psy_calendar_event', sa.Column('slot', sa.String(length=50), nullable=True))
    op.drop_constraint('psy_calendar_event_ibfk_1', 'psy_calendar_event', type_='foreignkey')
    op.drop_column('psy_calendar_event', 'event')
    op.drop_column('psy_calendar_event', 'user_id')
    op.drop_column('psy_calendar_event', 'start_date')
    op.drop_column('psy_calendar_event', 'end_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('psy_calendar_event', sa.Column('end_date', mysql.DATETIME(), nullable=False))
    op.add_column('psy_calendar_event', sa.Column('start_date', mysql.DATETIME(), nullable=True))
    op.add_column('psy_calendar_event', sa.Column('user_id', mysql.VARCHAR(length=50), nullable=True))
    op.add_column('psy_calendar_event', sa.Column('event', mysql.VARCHAR(length=50), nullable=False))
    op.create_foreign_key('psy_calendar_event_ibfk_1', 'psy_calendar_event', 'psy_user', ['user_id'], ['id'])
    op.drop_column('psy_calendar_event', 'slot')
    op.drop_column('psy_calendar_event', 'appointment_date')
    op.drop_column('psy_calendar_event', 'summary')
    # ### end Alembic commands ###

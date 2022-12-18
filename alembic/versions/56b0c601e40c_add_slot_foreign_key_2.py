"""Add slot foreign key 2

Revision ID: 56b0c601e40c
Revises: f23c1bef7cf0
Create Date: 2022-12-18 19:25:01.168474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b0c601e40c'
down_revision = 'f23c1bef7cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('psy_calendar_event_ibfk_1', 'psy_calendar_event', 'psy_slot', ['slot_id'], ['id'])
pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('psy_calendar_event_ibfk_1', 'psy_calendar_event', type_='foreignkey')
    pass
    # ### end Alembic commands ###

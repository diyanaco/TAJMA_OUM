"""empty message

Revision ID: e8bca7f54343
Revises: ff561ae85ced
Create Date: 2022-12-18 19:47:14.003865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8bca7f54343'
down_revision = 'ff561ae85ced'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('psy_calendar_event', sa.Column('slot_id', sa.String(length=50), nullable=True))
    op.create_foreign_key('psy_calendar_event_ibfk_1', 'psy_calendar_event', 'psy_slot', ['slot_id'], ['id'])
    pass


def downgrade():
    op.drop_constraint('psy_calendar_event_ibfk_1', 'psy_calendar_event', type_='foreignkey')
    op.drop_column('psy_calendar_event', 'slot_id')
    pass

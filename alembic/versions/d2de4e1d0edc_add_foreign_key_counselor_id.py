"""Add foreign key counselor_id

Revision ID: d2de4e1d0edc
Revises: 48646b910dc7
Create Date: 2023-01-22 12:22:12.826342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2de4e1d0edc'
down_revision = '48646b910dc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('psy_slot', sa.Column('counselor_id', sa.String(length=50), nullable=True))
    op.create_foreign_key(None, 'psy_slot', 'psy_user', ['counselor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'psy_slot', type_='foreignkey')
    op.drop_column('psy_slot', 'counselor_id')
    # ### end Alembic commands ###

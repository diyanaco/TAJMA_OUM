"""added test in user

Revision ID: 4ce846c07649
Revises: 64c0c9a48789
Create Date: 2022-12-26 09:15:26.040423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce846c07649'
down_revision = '64c0c9a48789'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('psy_user', sa.Column('test', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('psy_user', 'test')
    # ### end Alembic commands ###

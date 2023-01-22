"""change to time datatype3

Revision ID: 48646b910dc7
Revises: ff931d4ae4c8
Create Date: 2023-01-22 11:12:07.068858

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '48646b910dc7'
down_revision = 'ff931d4ae4c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('psy_slot', 'start_slot',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
    op.alter_column('psy_slot', 'end_slot',
               existing_type=mysql.DATETIME(),
               type_=sa.Time(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('psy_slot', 'end_slot',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('psy_slot', 'start_slot',
               existing_type=sa.Time(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    # ### end Alembic commands ###

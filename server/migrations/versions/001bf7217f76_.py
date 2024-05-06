"""empty message

Revision ID: 001bf7217f76
Revises: 5fe9eb633610
Create Date: 2024-04-18 13:10:00.241936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001bf7217f76'
down_revision = '5fe9eb633610'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('salary', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###

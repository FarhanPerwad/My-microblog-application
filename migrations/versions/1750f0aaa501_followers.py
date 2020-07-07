"""followers

Revision ID: 1750f0aaa501
Revises: 61400b3e4118
Create Date: 2020-07-01 20:46:45.676115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1750f0aaa501'
down_revision = '61400b3e4118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

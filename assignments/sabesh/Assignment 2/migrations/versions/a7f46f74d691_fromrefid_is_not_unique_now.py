"""fromrefID is not unique now

Revision ID: a7f46f74d691
Revises: 0965d2d474b6
Create Date: 2020-06-01 18:04:13.698497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7f46f74d691'
down_revision = '0965d2d474b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_fromrefID', table_name='user')
    op.create_index(op.f('ix_user_fromrefID'), 'user', ['fromrefID'], unique=False)
    op.drop_column('user', 'refID')
    op.drop_column('user', 'xrefID')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('xrefID', sa.VARCHAR(length=64), nullable=True))
    op.add_column('user', sa.Column('refID', sa.VARCHAR(length=64), nullable=True))
    op.drop_index(op.f('ix_user_fromrefID'), table_name='user')
    op.create_index('ix_user_fromrefID', 'user', ['fromrefID'], unique=1)
    # ### end Alembic commands ###

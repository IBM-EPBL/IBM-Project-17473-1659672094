"""Changed refID to ReferalCode table name

Revision ID: 85d99c29bc92
Revises: f9dfdbf9d0b1
Create Date: 2020-05-23 14:46:40.086073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85d99c29bc92'
down_revision = 'f9dfdbf9d0b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('referalcode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('referalID', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_referalcode_referalID'), 'referalcode', ['referalID'], unique=True)
    op.drop_index('ix_refID_refID', table_name='refID')
    op.drop_table('refID')
    op.add_column('user', sa.Column('lastname', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=True)
    op.drop_column('user', 'refID')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('refID', sa.VARCHAR(length=64), nullable=True))
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_column('user', 'lastname')
    op.create_table('refID',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('refID', sa.VARCHAR(length=64), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_refID_refID', 'refID', ['refID'], unique=1)
    op.drop_index(op.f('ix_referalcode_referalID'), table_name='referalcode')
    op.drop_table('referalcode')
    # ### end Alembic commands ###

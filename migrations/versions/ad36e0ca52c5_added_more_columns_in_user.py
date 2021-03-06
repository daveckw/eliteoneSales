"""Added more columns in User

Revision ID: ad36e0ca52c5
Revises: 984494ad8179
Create Date: 2019-04-18 01:32:39.512689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad36e0ca52c5'
down_revision = '984494ad8179'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
  
    op.add_column('user', sa.Column('phone_number', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('referrer_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_referrer_id'), 'user', ['referrer_id'], unique=False)
    op.create_unique_constraint(None, 'user', ['phone_number'])
    op.create_unique_constraint(None, 'user', ['ic_number'])
    op.create_foreign_key(None, 'user', 'user', ['referrer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_index(op.f('ix_user_referrer_id'), table_name='user')
    op.drop_column('user', 'referrer_id')
    op.drop_column('user', 'phone_number')
    op.drop_column('user', 'ic_number')
    op.drop_column('user', 'fullname')
    op.drop_column('user', 'date_created')
    op.drop_column('user', 'birthday')
    # ### end Alembic commands ###

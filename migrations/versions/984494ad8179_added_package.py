"""Added package

Revision ID: 984494ad8179
Revises: 136f718ddc3b
Create Date: 2019-04-17 09:27:17.819717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '984494ad8179'
down_revision = '136f718ddc3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_sale', sa.Column('created_by', sa.Text(), nullable=True))
    op.add_column('project_sale', sa.Column('package', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_sale', 'package')
    op.drop_column('project_sale', 'created_by')
    # ### end Alembic commands ###

"""empty message

Revision ID: 0d3ca3fb6039
Revises: 1628691a9630
Create Date: 2024-06-12 22:13:20.274657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d3ca3fb6039'
down_revision = '1628691a9630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('manufacturer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_contact', sa.String(length=15), nullable=False))
        batch_op.drop_column('business_phno')

    with op.batch_alter_table('recycler', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_contact', sa.String(length=15), nullable=False))
        batch_op.drop_column('business_phno')

    with op.batch_alter_table('retailer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_contact', sa.String(length=15), nullable=False))
        batch_op.drop_column('business_phno')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('retailer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_phno', sa.VARCHAR(length=15), nullable=False))
        batch_op.drop_column('business_contact')

    with op.batch_alter_table('recycler', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_phno', sa.VARCHAR(length=15), nullable=False))
        batch_op.drop_column('business_contact')

    with op.batch_alter_table('manufacturer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('business_phno', sa.VARCHAR(length=15), nullable=False))
        batch_op.drop_column('business_contact')

    # ### end Alembic commands ###
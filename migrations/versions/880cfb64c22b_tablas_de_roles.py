"""Tablas de roles.

Revision ID: 880cfb64c22b
Revises: 32db601317a5
Create Date: 2023-05-01 01:43:30.667275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '880cfb64c22b'
down_revision = '32db601317a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xxart_user_role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('role_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('xxart_user_role_name_key', type_='unique')
        batch_op.create_unique_constraint(None, ['role_id'])
        batch_op.create_unique_constraint(None, ['user_id'])
        batch_op.create_foreign_key(None, 'xxart_user', ['user_id'], ['id'])
        batch_op.create_foreign_key(None, 'xxart_role', ['role_id'], ['id'])
        batch_op.drop_column('description')
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xxart_user_role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.Integer(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('description', sa.Integer(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('xxart_user_role_name_key', ['name'])
        batch_op.drop_column('role_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
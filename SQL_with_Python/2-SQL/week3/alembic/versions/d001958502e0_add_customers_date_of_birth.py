"""add customers date_of_birth

Revision ID: d001958502e0
Revises: 51c855dc244c
Create Date: 2022-05-19 10:41:58.211879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd001958502e0'
down_revision = '51c855dc244c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )

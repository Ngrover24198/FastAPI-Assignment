"""init

Revision ID: a53de2464830
Revises: 
Create Date: 2023-07-07 13:27:36.591866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a53de2464830'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'assignment',     
        sa.Column('source_id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('source', sa.String(length=200), nullable=True),
        sa.Column('source_type', sa.String(length=10), nullable=True),
        sa.Column('source_tag', sa.String(length=10), nullable=True),
        sa.Column('last_updated_date', sa.DateTime(), nullable=True),
        sa.Column('from_date', sa.DateTime(), nullable=True),
        sa.Column('to_date', sa.DateTime(), nullable=True),
        sa.Column('frequency', sa.String(length=5), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('assignment')

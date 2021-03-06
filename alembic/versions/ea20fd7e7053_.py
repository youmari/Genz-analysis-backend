"""empty message

Revision ID: ea20fd7e7053
Revises: d58b08a56286
Create Date: 2022-06-18 14:06:26.212336

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ea20fd7e7053'
down_revision = 'd58b08a56286'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_sentences_analysis_category', table_name='sentences_analysis')
    op.drop_index('ix_young_people_analysis_logits', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_logits_mean', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_ma_logits', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_ma_net_sent', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_1', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_3', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_5', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_net_sent', table_name='young_people_analysis')
    op.drop_index('ix_young_people_analysis_net_sent_mean', table_name='young_people_analysis')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

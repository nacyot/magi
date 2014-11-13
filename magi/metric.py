""":mod:`magi.metric` --- Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import uuid

from sqlalchemy import types
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import Column, ForeignKey, ForeignKeyConstraint

from .orm import Base


CASCADE = 'CASCADE'


class Agent(Base):
    """Represent the individual Magi agent"""
    id = Column(postgresql.UUID, primary_key=True, default=uuid.uuid4)


class Metric(Base):
    """Represent the metrics sent from the Magi agent"""
    agent_id = Column(ForeignKey(Agent.id,
                                 onupdate=CASCADE,
                                 ondelete=CASCADE),
                      primary_key=True)
    id = Column(types.String(80), primary_key=True)
    target_id = Column(types.Unicode(80), nullable=False)
    plugin_name = Column(types.String(80), nullable=True)
    metric_name = Column(types.String(40), nullable=True)
    updated_at = Column(types.DateTime, nullable=False)
    data = Column(postgresql.JSON, nullable=False)


class Log(Base):
    """Raw data of each metrics"""
    agent_id = Column(primary_key=True)
    metric_id = Column(primary_key=True)
    timestamp = Column(types.DateTime, primary_key=True)
    key = Column(types.Unicode(256), nullable=True)
    value = Column(postgresql.JSON, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            [agent_id, metric_id],
            [Metric.agent_id, Metric.id],
            onupdate=CASCADE, ondelete=CASCADE,
        ),
        {}
    )

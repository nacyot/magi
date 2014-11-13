""":mod:`magi.metric` --- Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import uuid

from sqlalchemy.types import DateTime, String, Unicode
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.schema import Column, ForeignKey, ForeignKeyConstraint

from .orm import Base


CASCADE = 'CASCADE'


class Agent(Base):
    """Represent the individual Magi agent"""
    id = Column(UUID, primary_key=True, default=uuid.uuid4)

    __tablename__ = 'agents'


class Metric(Base):
    """Represent the metrics sent from the Magi agent"""
    agent_id = Column(ForeignKey(Agent.id,
                                 onupdate=CASCADE,
                                 ondelete=CASCADE),
                      primary_key=True)
    id = Column(String(80), primary_key=True)
    target_id = Column(Unicode(80), nullable=False)
    plugin_name = Column(String(80), nullable=True)
    metric_name = Column(String(40), nullable=True)
    updated_at = Column(DateTime, nullable=False)
    data = Column(JSON, nullable=False)

    __tablename__ = 'metrics'


class Log(Base):
    """Raw data of each metrics"""
    agent_id = Column(primary_key=True)
    metric_id = Column(primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    key = Column(Unicode(256), nullable=True)
    value = Column(JSON, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            [agent_id, metric_id],
            [Metric.agent_id, Metric.id],
            onupdate=CASCADE, ondelete=CASCADE,
        ),
        {}
    )

    __tablename__ = 'logs'

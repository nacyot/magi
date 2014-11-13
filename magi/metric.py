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
    __tablename__ = 'agents'

    #: Unique identifier of the agent
    #:
    #: Each agent will choose appropriate id, and send it to the headquarter
    #: to identify themselves.
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(Unicode(80), nullable=False)


class Metric(Base):
    """Represent the metrics sent from the Magi agent"""
    __tablename__ = 'metrics'

    agent_id = Column(ForeignKey(Agent.id,
                                 onupdate=CASCADE,
                                 ondelete=CASCADE),
                      primary_key=True)
    #: Unique identifier of each metric.
    id = Column(String(80), primary_key=True)
    target_id = Column(Unicode(80), nullable=False)
    metric_name = Column(String(40), nullable=False)
    updated_at = Column(DateTime, nullable=False)
    data = Column(JSON, nullable=False)


class Log(Base):
    """Raw data of each metrics"""
    __tablename__ = 'logs'

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

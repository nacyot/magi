""":mod:`magi.metric` --- Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import uuid

from sqlalchemy.types import DateTime, Unicode
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.schema import Column, ForeignKey, ForeignKeyConstraint

from .orm import Base


CASCADE = 'CASCADE'


class Agent(Base):
    """Magi agents."""
    __tablename__ = 'agents'

    #: (:class:`uuid.UUID`) The agent unique identifier.
    #: Each agent will choose appropriate id, and send it to the headquarter
    #: to identify themselves.
    id = Column(UUID, primary_key=True, default=uuid.uuid4)

    #: (:class:`str`) The agent name.
    name = Column(Unicode(80), nullable=False)


class Metric(Base):
    """Metrics from Magi agents."""
    __tablename__ = 'metrics'

    #: (:class:`uuid.UUID`) The :attr:`Agent.id`.
    agent_id = Column(ForeignKey(Agent.id,
                                 onupdate=CASCADE,
                                 ondelete=CASCADE),
                      primary_key=True)

    #: (:class:`str`) The metric unique identifier.
    id = Column(Unicode(80), primary_key=True)

    #: (:class:`str`) The target id.
    target_id = Column(Unicode(80), nullable=False)

    #: (:class:`str`) The metric name.
    metric_name = Column(Unicode(40), nullable=False)

    #: (:class:`datetime.datetime`) The updated time.
    updated_at = Column(DateTime, nullable=False)

    #: (:class:`dict`) The target id.
    data = Column(JSON, nullable=False)


class Log(Base):
    """Raw data of each metrics"""
    __tablename__ = 'logs'

    #: (:class:`uuid.UUID`) The :attr:`Agent.id`.
    agent_id = Column(primary_key=True)

    #: (:class:`str`) The :attr:`Metric.id`.
    metric_id = Column(primary_key=True)

    #: (:class:`datetime.datetime`) The log timestamp.
    timestamp = Column(DateTime, primary_key=True)

    #: (:class:`str`) The log key.
    key = Column(Unicode(256), nullable=True)

    #: (:class:`dict`) The log value.
    value = Column(JSON, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            [agent_id, metric_id],
            [Metric.agent_id, Metric.id],
            onupdate=CASCADE, ondelete=CASCADE,
        ),
        {}
    )

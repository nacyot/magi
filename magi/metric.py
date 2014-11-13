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
    """Magi agents."""

    #: (:class:`uuid.UUID`) The primary key UUID.
    id = Column(UUID, primary_key=True, default=uuid.uuid4)

    __tablename__ = 'agents'


class Metric(Base):
    """Metrics from Magi agents."""

    #: (:class:`uuid.UUID`) The :attr:`Agent.id`.
    agent_id = Column(ForeignKey(Agent.id,
                                 onupdate=CASCADE,
                                 ondelete=CASCADE),
                      primary_key=True)

    #: (:class:`basestring`) The metric id.
    id = Column(String(80), primary_key=True)

    #: (:class:`basestring`) The target id.
    target_id = Column(Unicode(80), nullable=False)

    #: (:class:`basestring`) The plugin name.
    plugin_name = Column(String(80), nullable=True)

    #: (:class:`basestring`) The metric name.
    metric_name = Column(String(40), nullable=True)

    #: (:class:`datetime.datetime`) The updated time.
    updated_at = Column(DateTime, nullable=False)

    #: (:class:`dict`) The target id.
    data = Column(JSON, nullable=False)

    __tablename__ = 'metrics'


class Log(Base):
    """Metric raw data."""

    #: (:class:`uuid.UUID`) The :attr:`Agent.id`.
    agent_id = Column(primary_key=True)

    #: (:class:`basestring`) The :attr:`Metric.id`.
    metric_id = Column(primary_key=True)

    #: (:class:`datetime.datetime`) The log timestamp.
    timestamp = Column(DateTime, primary_key=True)

    #: (:class:`basestring`) The log key.
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

    __tablename__ = 'logs'

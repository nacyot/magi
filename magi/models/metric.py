""":mod:`magi.models.metric` --- Models about logging metrics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy import types
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import Column

from ..orm import Base


class Host(Base):
    id = Column(postgresql.UUID, primary_key=True, default=uuid.uuid4)
    hostname = Column(types.String(48), nullable=True)


class Metric(Base):
    """"""
    host_id = Column(ForeignKey(Host.id), primary_key=True)
    id = Column(types.String(80), primary_key=True)
    plugin_name = Column(types.String(80), nullable=True)
    updated_at = Column(types.DateTime, nullable=False)
    data = Column(postgresql.JSON, nullable=False)


class Log(Base):
    """"""
    host_id = Column(ForeignKey(Metric.host_id), primary_key=True)
    metric_id = Column(ForeignKey(Metric.id,
                                  onupdate='CASCADE',
                                  ondelete='CASCADE'),
                       primary_key=True)
    timestamp = Column(types.DateTime, primary_key=True)
    value = Column(postgresql.JSON, nullable=False)

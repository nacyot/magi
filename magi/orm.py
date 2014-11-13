""":mod:`magi.orm` --- Object-relational mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


__all__ = ['Base', 'Session']


class Base(declarative_base()):
    """SQLAlchemy declarative base class"""
    __abstract__ = True


#: SQLAlchemy session class.
Session = sessionmaker()

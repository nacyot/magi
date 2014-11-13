""":mod:`magi.web.db` --- Database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use :data:`session` in view functions.

"""
from flask import current_app, g
from sqlalchemy import create_engine
from werkzeug.local import LocalProxy

from ..orm import Session


def get_session():
    """Gets a session.  If there's none yet, creates one.

    :returns: A session
    :rtype: :class:`magi.orm.Session`

    """
    if not hasattr(g, 'session'):
        engine = create_engine(current_app.config['DATABASE_URL'])
        g.session = Session(bind=engine)
    return g.session


def close_session(exception):
    """Closes an established session."""
    if hasattr(g, 'session'):
        g.session.close()


def setup_session(app):
    """Sets up ``app`` to be able to use :data:`session`.

    :param app: The Flask application to set up.
    :type app: :class:`~flask.Flask`

    """
    app.teardown_appcontext(close_session)


#: (:class:`~werkzeug.local.LocalProxy` of :class:`~magi.orm.Session`)
#: The context local session. Use this.
session = LocalProxy(get_session)

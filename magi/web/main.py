""":mod:`magi.web.main` --- Main pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, render_template


bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    """Home."""
    return render_template('home.html')

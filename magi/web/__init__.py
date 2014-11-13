""":mod:`magi.web` --- Magi web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Flask, render_template

from .db import setup_session


app = Flask(__name__)

setup_session(app)


@app.route('/')
def home():
    """Home."""
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)

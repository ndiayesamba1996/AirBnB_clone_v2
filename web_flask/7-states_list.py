#!/usr/bin/python3
""" A script thats starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exc):
    """ Removes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states_list')
def states_list():
    """
    Display a HTML page: (inside the tag BODY)
    - displays all State objects in DBStorage.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

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


@app.route('/states')
def states():
    """
    Display a HTML page: (inside the tag BODY)
    - displays all States in DBStorage.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """Display an HTML page for states or a specific state with its cities"""
    states = list(storage.all(State).values())
    selected_state = None
    if id:
        selected_state = next((state for state in states if state.id == id), None)
    return render_template('9-states.html', states=states, id=id, selected_state=selected_state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

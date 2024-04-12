#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """Display a HTML page for states or a specific state with its cities"""
    states = storage.all(State).values()
    # Sorting states by name
    states_sorted = sorted(states, key=lambda x: x.name)
    if id:
        # Finding the specific state by id after sorting
        state = next((state for state in states_sorted if state.id == id), None)
        # If state is found, sort its cities by name
        if state:
            state.cities = sorted(state.cities, key=lambda x: x.name) if hasattr(state, 'cities') else []
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', states=states_sorted)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

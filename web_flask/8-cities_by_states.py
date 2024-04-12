#!/usr/bin/python3
"""Starts a Flask web application with:
- States and cities listed
- Data from the storage engine
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # Fetch all State objects, sorted by name
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    # For each State, sort its cities by name
    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#!/usr/bin/python3
"""Write a script that starts a
Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello_8():
    states_dict = storage.all(State)
    return render_template('7-states_list.html', states=states_dict.values())


@app.teardown_appcontext
def s_close(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask

""" Crear una nueva instancia de Flask"""
app = Flask(__name__)

""" Define the principal route ("/") with the message "Hello HBNB!" """


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    """
    Configure app to listen in 0.0.0.0 in port 5000
    """
    app.run(host='0.0.0.0', port=5000)

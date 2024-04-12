#!/usr/bin/python3
""" Script to start a Flask web app """

from flask import Flask, render_template
from urllib.parse import unquote_plus

""" Create new Flask instance`"""
app = Flask(__name__)

""" Define the principal route ("/") with the message "Hello HBNB!" """


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    text = unquote_plus(text.replace('_', ' '))
    return (f"C {text}")


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_display(text):
    text = unquote_plus(text.replace('_', ' '))
    return (f"Python {text}")


@app.route('/number/<int:n>', strict_slashes=False)
def n_display(n):
    return (f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def templ_display(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    if n % 2 == 0:
        rslt = 'even'
    else:
        rslt = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, result=rslt)


if __name__ == '__main__':
    """
    Configure app to listen in 0.0.0.0 in port 5000
    """
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" A script thats starts a Flask web application."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ A function that returns the string 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A function that returns the string 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    A function that display 'C' followed by the value
    of the text variable.
    """
    return "C " + str(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
def python_default_text():
    """ Displays the python route default string."""
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    A function that displays 'Python',
    followed by the value of the text variable
    """
    return "Python " + str(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Displays 'n is a number' only if n is an integer."""
    return "%d is a number" % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

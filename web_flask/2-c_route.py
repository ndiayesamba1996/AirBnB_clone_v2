#!/usr/bin/python3
""" A script thats starts a Flask web application."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ a function that returns the string 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a function that returns the string 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def my_text(text):
    """a function that display 'C' followed by the value
    of the text variable."""
    return 'C ' + str(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

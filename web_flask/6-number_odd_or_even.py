#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" on the root route.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" on the /hbnb route.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Display "C " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.
    """
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Display "Python " followed by the value of the text variable.
    Replace underscore (_) symbols with a space.
    Default value of text is "is cool".
    """
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Display “n is a number” only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer.
    H1 tag: “Number: n” inside the tag BODY.
    """
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer.
    H1 tag: “Number: n is even|odd” inside the tag BODY.
    """
    return render_template(
            '6-number_odd_or_even.html',
            number=n,
            parity='even' if n % 2 == 0 else 'odd'
            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

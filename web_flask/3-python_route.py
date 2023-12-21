#!/usr/bin/python3
"""  a script that starts a Flask web application: """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns a text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Returns an other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replaces text with a variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replaces more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

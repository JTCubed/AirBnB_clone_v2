#!/usr/bin/python3
""" a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return ("HBNB")


@app.route('/c/<var>')
def Ctext(var):
    """returns C and text as a variable"""
    j = ""
    for i in var:
        if i == '_':
            i = ' '
        j = j + i
    return ("C {}".format(j))


@app.route('/python')
@app.route('/python/<var>')
def pythonf(var='is cool'):
    """returns Python and a variable text. Is cool being default"""
    j = ''
    for i in var:
        if i == '_':
            i = " "
        j = j + i
    return ("Python {}".format(j))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

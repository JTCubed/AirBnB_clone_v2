#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """returns Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return ("HBNB")


@app.route('/c/{var}')
def Cisfun(var):
    """returns C {} and variable text"""
    return ("C {}".format(var))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<var>')
def pythonf(var="is cool"):
    """returns Python and text as a variable, 'is cool' being default"""
    var.replace('_', ' ')
    return ("Python {}".format(var))


@app.route('/number/<int:var>')
def numberf(var):
    """returns <var> is a number if it is"""
    return (f"{var} is a number")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

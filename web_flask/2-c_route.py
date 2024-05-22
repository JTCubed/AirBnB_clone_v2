#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return ("HBNB")


@app.route('/c/<v>')
def Cisfun(v):
    """returns C and a variable text"""
    j = ''
    for i in v:
        if i == '_':
            i = " "
        j = j + i
    return ("C {}".format(j))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

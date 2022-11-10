#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"

@app.route('/c/<string:text>', strict_slash=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def extra_steps():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def simple():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def icky(text):
    return "C " + text.replace("_", " ")

@app.route("/python/<text>", strict_slashes=False)
def monty(text):
    text = "is cool"
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def pretty_ricky(n):
    if isinstance(n, int):
        return n + " is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/env python3

"""
Basic flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Home page with hello world text
    """
    return render_template("0-index.html")

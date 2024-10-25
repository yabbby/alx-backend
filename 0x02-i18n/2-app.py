#!/usr/bin/env python3

"""
Basic flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """
    Home page with hello world text
    """
    return render_template("0-index.html")


@babel.localeselector
def get_locale():
    """returns the correct locale"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])

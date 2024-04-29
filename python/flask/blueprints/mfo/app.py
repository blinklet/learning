# mfo/app.py

import flask
import mfo.home.views

def create_app():

    # Create app object
    app = flask.Flask(__name__)

    # Configure the app
    app.config.from_pyfile('config.py')

    # Register blueprints
    app.register_blueprint(mfo.home.views.bp)

    return app

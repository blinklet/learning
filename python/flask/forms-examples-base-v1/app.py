# app.py

import flask
import flask_bootstrap

import database
import views
import commands


def create_app():

    # Create app object
    app = flask.Flask(__name__)

    # Configure app
    app.config.from_pyfile('config.py', silent=True)

    # Register Bootstrap-Flask
    bootstrap = flask_bootstrap.Bootstrap5(app)

    # Register Flask-SQLAlchemy
    database.db.init_app(app)

    # Register blueprint
    app.register_blueprint(views.bp)
    app.register_blueprint(commands.bp)
        
    return app


if __name__ == "__main__":
    app.run()
    


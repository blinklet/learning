import flask
import database
import click


bp = flask.Blueprint('database', __name__,)

@bp.cli.command('create')
def create():
    database.create_database()
    database.add_test_data()
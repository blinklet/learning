# views.py

import flask
import sqlalchemy as sa
from database import db, Profile

bp = flask.Blueprint(
    'views',
    __name__,
    url_prefix='/',
    )

@bp.route('/')
def index():
    # get contents of DB
    profiles = db.session.scalars(
        db.select(Profile)
        ).all()

    return flask.render_template('/index.html', profiles=profiles)

@bp.route('/clean')
def clean():
    return flask.render_template('/clean.html')

@bp.route('/add')
def add_to():
    return flask.render_template('/add_to.html')

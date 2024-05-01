# mfo/home/views.py

import flask

bp = flask.Blueprint(
    'home',
    __name__,
    url_prefix='/',
    )

@bp.route('/')
def index():
    return flask.render_template('/home/index.html')

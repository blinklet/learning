import flask
from flask_bootstrap import Bootstrap5
import os
import database


app = flask.Flask(__name__)

# Configure app
app_dir = os.path.abspath(os.path.dirname(__file__))
app.config.update(
    ENVIRONMENT="Development",
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app_dir, 'data.db'),
)

# Register Bootstrap-Flask
bootstrap = Bootstrap5(app)

# Register Flask-SQLAlchemy
database.db.init_app(app)

# Register blueprint
import views
app.register_blueprint(views.bp)

# Create application database, if one does not already exist
with app.app_context():
    database.create_database()
    database.add_test_data()


if __name__ == "__main__":
    app.run()
    


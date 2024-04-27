# config.py

import os
import dotenv

dotenv.load_dotenv()

ENVIRONMENT = os.environ.get("FLASK_ENVIRONMENT")
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

if ENVIRONMENT == "development":
    app_dir = os.path.abspath(os.path.dirname(__file__))
    project_dir = os.path.dirname(app_dir)
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + 
        os.path.join(project_dir, "data.db")
        )
else:
     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

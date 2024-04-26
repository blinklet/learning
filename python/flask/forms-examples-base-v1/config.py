# config.py

import os
import dotenv

dotenv.load_dotenv()

ENVIRONMENT = os.environ.get("FLASK_ENVIRONMENT")
SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

if ENVIRONMENT == "development":
    app_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + 
        os.path.join(app_dir, "data.db")
        )
else:
     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

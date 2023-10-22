import os

from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

_database_server = os.getenv('DB_SERVER')
_database_port = os.getenv('DB_PORT')
_database_name = os.getenv('DB_NAME')
_database_userid = os.getenv('DB_UID')
_database_password = os.getenv('DB_PWD')

database_url = URL.create(
    drivername='postgresql+psycopg2',
    username=_database_userid,
    password=_database_password,
    host=_database_server,
    port=_database_port,
    database=_database_name
    )

# SQLite3 database
# database_url = "sqlite:////home/brian/db/userdata.db"
# database_url = "sqlite:///C:/Users/blinklet/Documents/learning/python/dbproject/userdata.db"

if __name__ == "__main__":
    print(f"Database URL = {database_url}")


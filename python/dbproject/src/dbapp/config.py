import os

from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

database_server = os.getenv('DB_SERVER')
database_port = os.getenv('DB_PORT')
database_name = os.getenv('DB_NAME')
database_userid = os.getenv('DB_UID')
database_password = os.getenv('DB_PWD')

database_url = URL.create(
    drivername='postgresql+psycopg2',
    username=database_userid,
    password=database_password,
    host=database_server,
    port=database_port,
    database=database_name
    )

# SQLite3 database
# database_url = "sqlite:////home/brian/db/userdata.db"

if __name__ == "__main__":
    print(database_url)


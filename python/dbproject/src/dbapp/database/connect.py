# dbapp/database/connect.py
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbapp import config


engine = create_engine(config.database_url)
Session = sessionmaker(engine)


if __name__ == "__main__":
    print(engine)
    with Session() as session:
        connection = session.connection()
        print(connection)


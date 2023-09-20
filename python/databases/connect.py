from sqlalchemy import create_engine


engine = db.create_engine('sqlite:///userdata.db')
metadata.create_all(engine)
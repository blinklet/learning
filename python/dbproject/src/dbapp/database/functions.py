from datetime import datetime

from sqlalchemy import select, update, delete

from dbapp.database.models import Userdata


def db_id_exists(session, id):
    stmt = (select(Userdata.user_id).where(Userdata.user_id == id))
    result = session.scalar(stmt)
    if result == None:
        return False
    else:
        return result

def db_write(session, id, data):
    userdata = Userdata(
        user_id = id,
        user_data = data,
        time_stamp = datetime.now()
    )
    session.add(userdata)


# https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
def db_update(session, id, data):
    stmt = (update(Userdata)
            .where(Userdata.user_id == id)
            .values(user_data=data, time_stamp = datetime.now()))
    session.execute(stmt)


# old ORM method using query
# def db_update(session, id, data):
#     row = session.query(Userdata).filter_by(user_id=id).first()
#     row.user_data = data
#     row.time_stamp = datetime.now()
#     # session.commit()


def db_read(session, id):
    if id == "all":
        stmt = select(Userdata)
    else:
        stmt = select(Userdata).where(Userdata.user_id == id)
    results = session.execute(stmt)
    return results
    

def db_delete(session, id):
    if db_id_exists(session, id):
        stmt = delete(Userdata).where(Userdata.user_id == id)
        session.execute(stmt)
        return True
    else:
        return False


if __name__ == "__main__":
    from dbapp.database.connect import Session
    from dbapp.database.models import db_setup
    db_setup()
    with Session() as session:
        db_write(session, "test_id1", "this is test data")
        if db_id_exists(session, "test_id1"):
          print("test_id1 written correctly")
        db_update(session, "test_id1", "New data")
        db_read(session, "test_id1")
        db_delete(session, "test_id1")
        if not db_id_exists(session, "test_id1"):
          print("test_id1 deleted correctly")
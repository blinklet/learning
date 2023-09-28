from dbapp.database.models import Userdata
from sqlalchemy import select, update
from tabulate import tabulate

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
        user_data = data
    )
    session.add(userdata)
    # session.commit()

#https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
def db_update(session, id, data):
    stmt = (update(Userdata)
            .where(Userdata.user_id == id)
            .values(user_data=data))
    x = session.execute(stmt)
    return x
    # session.commit()

# old ORM method using query
def db_update2(session, id, data):
    row = session.query(Userdata).filter_by(user_id=id).first()
    row.user_data = data
    # session.commit()



def db_read(session, id):
    stmt = (
        select(
            Userdata.user_id,
            Userdata.user_data,
            Userdata.time_stamp,
        )
    )
    if id != "all":
        stmt = stmt.where(Userdata.user_id == id)
    query = session.execute(stmt)
    return tabulate(query.fetchall(), headers=query.keys())


if __name__ == "__main__":
    from .connect import Session
    from pprint import pprint
    with Session() as session:
        print(db_id_exists(session, "test3"))
        print(db_id_exists(session, "test2"))
        pprint(db_update(session, "test3", "west"))
        pprint(db_update2(session, "beans", "east"))
        pprint(db_update(session, "not_existing", "test"))
        print(db_read(session, "other_not_exists"))

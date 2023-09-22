from .models import Userdata
from sqlalchemy import select, update
from tabulate import tabulate

def db_name_exists(session, name):
    stmt = (select(Userdata.user_name).where(Userdata.user_name == name))
    result = session.scalar(stmt)
    if result == None:
        return False
    else:
        return result

def db_write(session, name, data):
    userdata = Userdata(
        user_name = name,
        user_data = data
    )
    session.add(userdata)
    # session.commit()

#https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
def db_update(session, name, data):
    stmt = (update(Userdata)
            .where(Userdata.user_name == name)
            .values(user_data=data))
    x = session.execute(stmt)
    return x
    # session.commit()

# old ORM method using query
def db_update2(session, name, data):
    row = session.query(Userdata).filter_by(user_name=name).first()
    row.user_data = data
    # session.commit()



def db_read(session, name):
    if name == "all":
        stmt = (select(Userdata.user_name, Userdata.user_data))
    else:
        stmt = (select(Userdata.user_name, Userdata.user_data).where(Userdata.user_name == name))
    query = session.execute(stmt)
    return tabulate(query.fetchall(), headers=query.keys())


if __name__ == "__main__":
    from .connect import Session
    from pprint import pprint
    with Session() as session:
        print(db_name_exists(session, "test3"))
        print(db_name_exists(session, "test2"))
        pprint(db_update(session, "test3", "west"))
        pprint(db_update2(session, "beans", "east"))
        pprint(db_update(session, "not_existing", "test"))
        print(db_read(session, "other_not_exists"))

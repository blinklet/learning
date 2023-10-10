from dbapp.database.functions import db_read, db_update, db_write, db_id_exists, db_delete


def read(session, user_id_list):
    if "all" in user_id_list:
        results = db_read(session, "all").scalars()
        for row in results:
            print(row)
    else:
        for uid in user_id_list:
            result = db_read(session, uid).scalar()
            if result != None:
                print(db_read(session, uid).scalar())
            else:
                print(f"User '{uid}' does not exist")


def update(session, user_id, user_data):
        if db_id_exists(session, user_id):
            db_update(session, user_id, user_data)
            print(f"User '{user_id}' updated.")
        else:
            print(f"User '{user_id}' does not exist.")


def write(session, user_id, user_data):
    if db_id_exists(session, user_id):
        print(f"User '{user_id}' exists! Write operation cancelled.")
    else:
        db_write(session, user_id, user_data)
        print(f"New user '{user_id}' created.")


def delete(session, user_id_list):
    for uid in user_id_list:
        if db_id_exists(session, uid):
            db_delete(session, uid)
            print(f"User '{uid}' deleted")
        else:
            print(f"User '{uid}' does not exist.")
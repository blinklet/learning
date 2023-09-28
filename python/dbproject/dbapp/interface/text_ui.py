from dbapp.database.models import db_setup
from dbapp.database.functions import db_read, db_update, db_write, db_id_exists


QUIT = ["quit", "", "q", "exit"]


def read(session):
    while (uid := input("Search for a user's id or type 'all' to list all users: ").lower()) not in QUIT:
        if db_id_exists(session, uid) or uid == "all":
            return db_read(session, uid)
        else:
            return f"User '{uid}' does not exist. Try again."
    return "No data read."


def overwrite(session, uid):
    update = input(f"Do you want to overwrite {uid}'s user data (Y/N)?").lower()
    if update == "yes" or update == "y":
        data = input("Enter the user's data: ")
        if data not in QUIT:
            db_update(session, uid, data)
            return "User data overwritten."
    return "Data not overwritten."


def write(session):
    while (uid := input("Enter a user's id: ").lower()) not in QUIT:

        if db_id_exists(session, uid):
            return overwrite(session, uid)
        else:
            data = input("Enter the user's data: ")
            if data not in QUIT:
                db_write(session, uid, data)
                return "New user data created."
    return "No data written"


def main(session):
    while (mode := input("Do you want to read or write (R/W)? ").lower()) not in QUIT:
        if mode == "r" or mode == "read":
            print(read(session))
        elif mode == "w" or mode == "write":
            print(write(session))
    print("Thank you! Goodbye.")


if __name__ == "__main__":
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        main(session)
    
from dbapp.database.functions import db_read, db_update, db_write, db_id_exists, db_delete


QUIT = ["quit", "", "q", "exit"]


def read(session):
    while (uid := input("Search for a user's id or type 'all' to list all users: ").lower()) not in QUIT:
        if db_id_exists(session, uid) or uid == "all":
            db_read(session, uid)
        else:
            print(f"User '{uid}' does not exist. Try again or press Enter to cancel.")


def overwrite(session, uid):
    update = input(f"Do you want to overwrite {uid}'s user data (Y/N)?").lower()
    if update == "yes" or update == "y":
        data = input("Enter the user's data: ")
        if data not in QUIT:
            db_update(session, uid, data)
            print("User data overwritten.")
        else:
            print("Change cancelled.")
    else:
        print("Data not overwritten.")


def write(session):
    while (uid := input("Enter a user's id: ").lower()) not in QUIT:
        if db_id_exists(session, uid):
            overwrite(session, uid)
        else:
            data = input("Enter the user's data: ")
            if data not in QUIT:
                db_write(session, uid, data)
                print("New user data created.")
            else:
                print("Write cancelled")

def delete(session):
    while (uid := input("Select user id to delete: ").lower()) not in QUIT:
        if db_id_exists(session, uid):
            db_delete(session, uid)
        else:
            print(f"User '{uid}' does not exist. Try again or press Enter to cancel.")
    
def main(session):
    while (mode := input("Do you want to read, write, or delete (R/W/D)? ").lower()) not in QUIT:
        if mode == "r" or mode == "read":
            read(session)
        elif mode == "w" or mode == "write":
            write(session)
        elif mode == "d" or mode == "delete":
            delete(session)
        else:
            print("Please select either 'read', 'write', 'delete', or 'quit'.")
    print("Thank you! Goodbye.")


if __name__ == "__main__":
    from dbapp.database.models import db_setup
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        main(session)
    
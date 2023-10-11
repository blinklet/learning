from dbapp.interface.functions import read, update, write, delete

"""
Maybe re-write using cmd module?
https://docs.python.org/3/library/cmd.html
"""

QUIT = ["quit", "", "q", "exit"]


def delete(session):
    while (uid := input("Select user id to delete: ").lower()) not in QUIT:
        if db_id_exists(session, uid):
            db_delete(session, uid)
        else:
            print(f"User '{uid}' does not exist. Try again or press Enter to cancel.")
    
def main(session):
    while (mode := input("Do you want to read, write, update, or delete (R/W/U/D)? ").lower()) not in QUIT:
        if mode == "r" or mode == "read":
            while (uid := input("Search for a user's id or type 'all' to list all users: ").lower()) not in QUIT:
                read(session, [uid])   # because read function expects a list
        elif mode == "w" or mode == "write":
            while (uid := input("Enter a user's id: ").lower()) not in QUIT:
                data = input("Enter the user's data: ")
                write(session, uid, data)
        elif mode == "u" or mode == "update":
            while (uid := input("Enter a user's id: ").lower()) not in QUIT:
                data = input("Enter the user's data: ")
                update(session, uid, data)
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
    
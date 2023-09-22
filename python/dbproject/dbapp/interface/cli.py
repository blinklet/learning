from ..database.models import db_setup
from ..database.functions import db_read, db_update, db_write, db_name_exists
from ..database.connect import Session

def main(session):
    quit = ["quit", "", "q", "exit"]
    while (mode := input("Do you want to read or write (R/W)? ").lower()) not in quit:
        if mode == "r" or mode == "read":
            while (name := input("Search for a user's name or type 'all' to list all users: ").lower()) not in quit:
                if name == "all":
                    print(db_read(session, name))
                elif db_name_exists(session, name):
                    print(db_read(session, name))
                else:
                    print(f"User '{name}' does not exist. Try again.")
        elif mode == "w" or mode == "write":
            while (name := input("Enter a user's name: ").lower()) not in quit:
                data = input("Enter the user's data: ")
                if data in quit:
                    print("Data not written.")
                    break
                if db_name_exists(session, name):
                    overwrite = input(f"Do you want to overwrite {name}'s user data (Y/N)?").lower()
                    if overwrite == "yes" or overwrite == "y":
                        db_update(session, name, data)
                        print("User data overwritten.")
                else:
                    db_write(session, name, data)
                    print("New user data created.")
    print("Thank you! Goodbye.")

if __name__ == "__main__":
    db_setup()
    with Session.begin() as session:
        main(session)
    
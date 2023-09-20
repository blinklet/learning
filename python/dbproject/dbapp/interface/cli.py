from . import db
from ..dbsetup.models import db_setup

def handle_data(name, data=""):

    if db.db_check(name) == "name_conflict":
        overwrite = input(f"Do you want to overwrite {name}'s user data (Y/N)?")
        if overwrite == "Y" or overwrite == "y":
            db.db_update(name, data)
    else:
        db.db_write(name, data)
        
def main():

    while (name := input("Enter a user's name: ").lower()) != "quit":
        data = input("Enter the user's data: ")
        handle_data(name, data)
    else:
        print("Thank you for entering data!")

if __name__ == "__main__":
    db_setup()
    main()
    
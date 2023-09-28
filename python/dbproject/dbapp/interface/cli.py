"""
dbapp -r all
dbapp -r brian
dbapp -w brian datadatyadat
   (could fail due to existing user)
   (ask if OK to overwrite)
dbapp -w -f brian datadatyadat
dbapp -d brian
dbapp -d all   
    (are you sure?)
"""

import yaml, sys, os

from dbapp import interface

valid_args = ["-i",
                "--interactive",
                "-r",
                "--read",
                "w",
                "write",
                "-f",
                "--force",
                "-wf",
                "-fw",
                "-d",
                "--delete",
                ]

def valid(argument):
    if argument in valid_args:
        return True
    else:
        return False


def read_data(uid):
    pass


def write_data(uid):
    pass


def main():


    # Make a copy of the argument list with the program name removed
    args = sys.argv[1:]

    arg_list = [] 
    while args:
        arg_list.append(args.pop(0))

    while args:
        argument = args.pop(0)
        if valid(argument): 
            if argument == '-i' or argument == '--interactive':
                interface.text_ui()
            elif argument == '-r' or argument == '--read':
                uid = args.pop(0)
                read_data(uid)
            elif argument == '-w' or argument == '--write':
                uid = args.pop(0)
                write_data(uid, args)
            elif argument == '-w' or argument == '--write':



        elif argument == '-o' or argument == '--output':
            output_file = args.pop(0)
            output_dir = os.path.dirname(output_file)
            if output_dir:
                if not os.path.exists(output_dir):
                    print('Output file directory does not exist!')
                    sys.exit(2)
        elif argument == '-h' or argument == '--help':
            print(help_text)
            sys.exit(0)
        else:
            print('Invalid arguments!')
            print(help_text)
            sys.exit(2)



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
    
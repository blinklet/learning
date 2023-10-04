
"""Database Application.

Usage: 
  dbapp.py read <name>...
  dbapp.py write <name> <data>
  dbapp.py update <name> <data>
  dbapp.py delete <name>...
  dbapp.py -i | --interactive
  dbapp.py -h | --help
  dbapp.py -v | --version

Options:
  -h --help         Show this help message and exit
  -i --interactive  Switch to interactive mode
  --version         Show program version and exit
"""

from docopt import docopt

from dbapp.database.functions import db_read, db_update, db_write, db_id_exists, db_delete

def read(session, user_id_list):
    for uid in user_id_list:
        if db_id_exists(session, uid) or uid == "all":
            db_read(session, uid)
        else:
            print(f"User '{uid}' does not exist.")


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


def main(session):
    arguments = docopt(__doc__, version='DB App 1.0')
    if arguments["--interactive"] == True:
        from dbapp.interface import text_ui
        text_ui.main(session)
    elif arguments["read"] == True:
        read(session, arguments["<name>"])
    elif arguments["write"] == True:
        write(session, arguments["<name>"][0], arguments["<data>"])
    elif arguments["update"] == True:
        update(session, arguments["<name>"][0], arguments["<data>"])
    elif arguments["delete"] == True:
        delete(session, arguments["<name>"])
    else:
        exit("That is not a valid command. See 'dbapp --help'.")
        # This is here just in case docopt changes the way
        # it parses commands

  

if __name__ == "__main__":
    from dbapp.database.models import db_setup
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        main(session)
    
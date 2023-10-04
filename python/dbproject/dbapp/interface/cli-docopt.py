
"""Database Application.

Usage:
  dbapp.py -i | --interactive
  dbapp.py read NAME...
  dbapp.py write NAME DATA
  dbapp.py update NAME DATA
  dbapp.py delete NAME...
  dbapp.py -h | --help
  dbapp.py --version

Options:
  -h --help            show this help message and exit
  -i --interactive     Switch to interactive mode
  ---version         show program's version number and exit
"""

"""
usage: git [--version] [--exec-path=<path>] [--html-path]
           [-p|--paginate|--no-pager] [--no-replace-objects]
           [--bare] [--git-dir=<path>] [--work-tree=<path>]
           [-c <name>=<value>] [--help]
           <command> [<args>...]

options:
   -c <name=value>
   -h, --help
   -p, --paginate

The most commonly used git commands are:
   add        Add file contents to the index
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   push       Update remote refs along with associated objects
   remote     Manage set of tracked repositories

See 'git help <command>' for more information on a specific command.
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
    print(arguments)

    # parser = argparse.ArgumentParser(
    #     description="Database Application"
    #     )
    # subparsers = parser.add_subparsers(
    #     title='subcommands', 
    #     dest='subparser_name'
    #     )

    # read_parser = subparsers.add_parser(
    #     'read', 
    #     aliases=['r'], 
    #     help="Display rows that match names. Default action."
    #     )
    # read_parser.add_argument('user_id_list', nargs='+')

    # write_parser = subparsers.add_parser(
    #     'write', 
    #     aliases=['w'], 
    #     help="Add new name and data.")
    # write_parser.add_argument('user_id')
    # write_parser.add_argument('user_data')

    # update_parser = subparsers.add_parser(
    #     'update', 
    #     aliases=['u'], 
    #     help="Update row that matches name with new data.")
    # update_parser.add_argument('user_id')
    # update_parser.add_argument('user_data')

    # delete_parser = subparsers.add_parser(
    #     'delete', 
    #     aliases=['d', 'del'], 
    #     help="Delete row that matches name(s).")
    # delete_parser.add_argument('user_id_list', nargs='+')

    # parser.add_argument(
    #     '-i', '--interactive', 
    #     action='store_true', 
    #     help="Switch to interactive mode")
    
    # parser.add_argument(
    #     '-v', '--version', 
    #     action='version', 
    #     version='dbapp 0.1')

    # args = parser.parse_args()

    # if args.interactive == True:
    #     from dbapp.interface import text_ui
    #     text_ui.main(session)

    match args.subparser_name:
        case 'read' | 'r': 
            read(session, args.user_id_list)
        case'write' | 'w': 
            write(session, args.user_id, args.user_data)
        case'update' | 'u': 
            update(session, args.user_id, args.user_data)
        case'delete' | 'del' | 'd': 
            delete(session, args.user_id_list)
  

if __name__ == "__main__":
    from dbapp.database.models import db_setup
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        main(session)
    
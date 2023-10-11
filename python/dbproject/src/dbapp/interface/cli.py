import argparse

from dbapp.interface.functions import read, write, update, delete

"""Database Application.

Usage: 
  dbapp.py read NAME...
  dbapp.py write NAME DATA
  dbapp.py update NAME DATA
  dbapp.py delete NAME...
  dbapp.py -i | --interactive
  dbapp.py -h | --help
  dbapp.py -v | --version

Options:
  -h --help         Show this help message and exit
  -i --interactive  Switch to interactive mode
  --version         Show program version and exit
"""

def main(session):

    parser = argparse.ArgumentParser(
        description="Database Application"
        )
    subparsers = parser.add_subparsers(
        title='subcommands', 
        dest='subparser_name'
        )

    read_parser = subparsers.add_parser(
        'read', 
        aliases=['r'], 
        help="Display rows that match names. Default action."
        )
    read_parser.add_argument('user_id_list', nargs='+')

    write_parser = subparsers.add_parser(
        'write', 
        aliases=['w'], 
        help="Add new name and data.")
    write_parser.add_argument('user_id')
    write_parser.add_argument('user_data')

    update_parser = subparsers.add_parser(
        'update', 
        aliases=['u'], 
        help="Update row that matches name with new data.")
    update_parser.add_argument('user_id')
    update_parser.add_argument('user_data')

    delete_parser = subparsers.add_parser(
        'delete', 
        aliases=['d', 'del'], 
        help="Delete row that matches name(s).")
    delete_parser.add_argument('user_id_list', nargs='+')

    parser.add_argument(
        '-i', '--interactive', 
        action='store_true', 
        help="Switch to interactive mode")    
    parser.add_argument(
        '-v', '--version', 
        action='version', 
        version='dbapp 0.1')

    args = parser.parse_args()

    if args.interactive == True:
        from dbapp.interface import text_ui
        text_ui.main(session)

    match args.subparser_name:
        case 'read' | 'r': 
            read(session, args.user_id_list)
        case 'write' | 'w': 
            write(session, args.user_id, args.user_data)
        case 'update' | 'u': 
            update(session, args.user_id, args.user_data)
        case 'delete' | 'del' | 'd': 
            delete(session, args.user_id_list)
        case None if not args.interactive:
            parser.print_help()


if __name__ == "__main__":
    from dbapp.database.models import db_setup
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        main(session)

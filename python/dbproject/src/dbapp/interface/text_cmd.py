import cmd
import re

from dbapp.database.functions import db_read, db_update, db_write, db_id_exists, db_delete
from dbapp.interface.cli import read, write, update, delete


def parse(arg):
    parsed_list = [] 
    # regex that finds single words (by themselves, or in quotes) 
    # or groups of words enclosed in quotes. 
    # Quotes may be single or double.
    items = re.findall(r'("[^"]*"|\'[^\']*\'|\b\w+\b)', arg)
    for item in items:
        if ((item.startswith('"') and item.endswith('"')) or 
                (item.startswith("'") and item.endswith("'"))):
            parsed_list.append(item.strip('"\''))
        else:
            parsed_list.append(item)
    return(parsed_list)

def two_params(params):
    if len(params) != 2:
        return False
    return True
    


class AppShell(cmd.Cmd):
    def __init__(self, session):
        super().__init__()
        self.session = session
        # https://stackoverflow.com/questions/12911327/aliases-for-commands-with-python-cmd-module
        self.aliases = { 'r' : self.do_read,
                         'w' : self.do_write,
                         'u' : self.do_update,
                         'd' : self.do_delete,
                         'q' : self.do_quit,
                         }
    
    intro = """
Welcome to dbapp, the Database Application.
Type help or ? to list commands.
"""
    prompt = "dbapp> "

    def do_read(self, arg):
        """Usage: read <name> [<name>]..."""
        if arg != "":
            read(self.session, parse(arg))
        else:
            self.onecmd('help read')

    def do_write(self, arg):
        """Usage: write <name> <data>"""
        params = parse(arg)
        if len(params) == 2: # check for just two arguments
            user_id, user_data = params
            write(self.session, user_id, user_data)
        else:
            self.onecmd("help write")

    def do_update(self, arg):
        """Usage: update <name> <data>"""
        params = parse(arg)
        if len(params) == 2: # check for just two arguments
            user_id, user_data = params
            update(self.session, user_id, user_data)
        else:
            self.onecmd("help update")

    def do_delete(self, arg):
        """Usage: delete <name> [<name>]..."""
        if arg != "":
            delete(self.session, parse(arg))
        else:
            self.onecmd('help delete')

    def do_quit(self, arg):
        """Usage: quit"""
        return True
     
    def do_help(self, arg):
        """List available commands."""
        if arg in self.aliases:
            arg = self.aliases[arg].__name__[3:]
        cmd.Cmd.do_help(self, arg)

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        print(cmd)
        if cmd in self.aliases:
            return self.aliases[cmd](arg) # quit returns "True", which exits the loop
        else:
            self.onecmd('help')

    def emptyline(self):
        """what to do for an empty line"""
        self.onecmd('help')

if __name__ == "__main__":
    from dbapp.database.models import db_setup
    from dbapp.database.connect import Session
    db_setup()
    with Session.begin() as session:
        app = AppShell(session)
        app.cmdloop()
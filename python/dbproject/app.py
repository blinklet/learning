from dbapp.interface import cli
from dbapp.database.models import db_setup
from dbapp.database.connect import Session

db_setup()

with Session.begin() as session:
    cli.main(session)

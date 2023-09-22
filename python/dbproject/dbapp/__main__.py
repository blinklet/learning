from .interface import cli
from .database.models import db_setup
from .database.connect import Session

db_setup()

with Session.begin() as session:
    cli.main(session)

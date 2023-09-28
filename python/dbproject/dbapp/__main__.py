from dbapp.interface import text_ui
from dbapp.database.models import db_setup
from dbapp.database.connect import Session

db_setup()

# https://docs.sqlalchemy.org/en/20/orm/session_basics.html#session-frequently-asked-questions
with Session.begin() as session:
    session.expire_on_commit = False
    text_ui.main(session)

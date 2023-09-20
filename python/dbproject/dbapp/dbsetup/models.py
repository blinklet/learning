from . import database
from sqlalchemy import Integer, String, UnicodeText
from sqlalchemy.orm import mapped_column


class Userdata(database.Base):
    __tablename__ = "userdata"

    id = mapped_column(Integer, primary_key=True)
    user_name = mapped_column(String(32), nullable=False)
    user_data = mapped_column(UnicodeText)

    def __repr__(self):
        return(self.user_name, self.user_data)

def db_setup():
    database.Base.metadata.create_all(database.engine)

if __name__ == "__main__":
    db_setup()
    
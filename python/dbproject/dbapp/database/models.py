from sqlalchemy import Integer, String, UnicodeText, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

from dbapp.database.connect import engine


Base = declarative_base()


class Userdata(Base):
    __tablename__ = "userdata"

    index = mapped_column(Integer)
    user_id = mapped_column(String(32), primary_key=True, nullable=False)
    user_data = mapped_column(UnicodeText)
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    time_stamp = mapped_column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return(self.user_id, self.user_data)


def db_setup():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_setup()
    
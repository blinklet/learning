from sqlalchemy import Integer, String, UnicodeText, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column
# from tabulate import tabulate

from dbapp.database.connect import engine


Base = declarative_base()


class Userdata(Base):
    __tablename__ = "userdata"

    user_id = mapped_column(String(32), primary_key=True, nullable=False)
    user_data = mapped_column(UnicodeText)
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    time_stamp = mapped_column(DateTime(timezone=True))
    # I used to have `, server_default=func.now()` in the DateTime column but
    # I chose to calculate datetime in my program because it is simpler to
    # update the timestamp in an existing row (other solution involves creating
    # a trigger in the SQL database as discussed in
    # https://stackoverflow.com/questions/22594567/sql-server-on-update-set-current-timestamp)

    # https://stackoverflow.com/questions/19258471/sqlalchemy-orm-init-method-vs
    def __init__(self, user_id, user_data, time_stamp):
        self.user_id = user_id
        self.user_data = user_data
        self.time_stamp = time_stamp

    def __repr__(self):
        return f"ID = {self.user_id:10}  " \
               f"DATA = {self.user_data:20}  " \
               f"TIME = {self.time_stamp.strftime('%B %d %H:%M')}"

    # def __repr__(self):
    #     output = ''
    #     for c in self.__table__.columns:
    #         output += f"{c.name}:::: {getattr(self, c.name)}\n"
    #     return output

def db_setup():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_setup()
    
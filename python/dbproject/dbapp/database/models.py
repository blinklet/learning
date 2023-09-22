from . import connect
from sqlalchemy import Integer, String, UnicodeText
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class Userdata(Base):
    __tablename__ = "userdata"

    id = mapped_column(Integer, primary_key=True)
    user_name = mapped_column(String(32), nullable=False)
    user_data = mapped_column(UnicodeText)

    def __repr__(self):
        return(self.user_name, self.user_data)


def db_setup():
    Base.metadata.create_all(connect.engine)


if __name__ == "__main__":
    db_setup()
    
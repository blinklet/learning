from sqlalchemy import Integer, Uuid, UnicodeText
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Userdata(Base):
    __tablename__ = "userdata"

    id = db.orm.mapped_column(Integer, primary_key=True)
    uuid = mapped_column(Uuid, nullable=False)
    user_data = mapped_column(UnicodeText)








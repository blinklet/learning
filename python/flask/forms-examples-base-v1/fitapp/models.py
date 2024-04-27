from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
import datetime

from fitapp.database import db

class Profile(db.Model):
    __tablename__="profiles"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str]
    height: Mapped[float]
    weight: Mapped[float]
    birthdate: Mapped[datetime.date]
    last_update: Mapped[datetime.datetime]
    __table_args__ = (
        UniqueConstraint('firstname', 'lastname', name='fullname_uc'),
    )
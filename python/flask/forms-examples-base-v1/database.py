# database.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


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
    

def create_database():
    db.create_all()


def add_test_data():
    test_data = [
        dict(
            firstname="Brad", lastname="Chadwick", email="brad@fakemail.com", 
            height=184.5, weight=90.25, birthdate=datetime.date(1999, 4, 15),
            last_update=datetime.datetime(2024, 5, 30, 13, 33, 56)
            ),
        dict(
            firstname="Lisa", lastname="Welstone", email="lisa@notmail.com", 
            height=163.0, weight=63.5, birthdate=datetime.date(1996, 12, 20),
            last_update=datetime.datetime(2024, 4, 15, 9, 30, 44)
            ),
        ]
    
    for row in test_data:
        profile = Profile(**row)
        db.session.add(profile)
        try:
            db.session.commit()
        except IntegrityError:
            print(f"Data for { row['firstname'] } { row['lastname'] } already exists")
            db.session.rollback()


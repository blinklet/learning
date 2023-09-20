from models import engine, Userdata
from sqlalchemy import select
from sqlalchemy.orm import Session

with Session(engine) as session:

    # create 4 random entries
    For x in 
...     spongebob = User(
...         name="spongebob",
...         fullname="Spongebob Squarepants",
...         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
...     )
...     sandy = User(
...         name="sandy",
...         fullname="Sandy Cheeks",
...         addresses=[
...             Address(email_address="sandy@sqlalchemy.org"),
...             Address(email_address="sandy@squirrelpower.org"),
...         ],
...     )
...     patrick = User(name="patrick", fullname="Patrick Star")
...
...     session.add_all([spongebob, sandy, patrick])
...
...     session.commit()

insertion_query = users.insert().values([
    {'first_name':'Tina', 'last_name':'McCoy', 'email_address':'tmccoy@hplusport.com'},
    {'first_name':'Joan', 'last_name':'Ruiz', 'email_address':'jruixm@hplusport.com'}
])

connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())
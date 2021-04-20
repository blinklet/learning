import sqlalchemy as db

engine = db.create_engine('sqlite:///users-sqlalchemy.db')

metadata = db.MetaData()

connection = engine.connect()

users = db.Table('Users', metadata, 
    db.Column('user_id', db.Integer, primary_key=True),
    db.Column('first_name', db.Text),
    db.Column('last_name', db.Text),
    db.Column('email_address', db.Text)
)

metadata.create_all(engine)

insertion_query = users.insert().values([
    {'first_name':'Tina', 'last_name':'McCoy', 'email_address':'tmccoy@hplusport.com'},
    {'first_name':'Joan', 'last_name':'Ruiz', 'email_address':'jruixm@hplusport.com'}
])

connection.execute(insertion_query)

selection_query = db.select([users.columns.email_address])
selection_result = connection.execute(selection_query)

print(selection_result.fetchall())

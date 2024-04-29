import flask
from sqlalchemy.exc import IntegrityError
import json
from datetime import datetime
import os
import click

import fitapp.database as database
import fitapp.models as models

bp = flask.Blueprint('database', __name__,)

@bp.cli.command('create')
def create():
    database.db.create_all()

@bp.cli.command('add-data')
@click.argument("filename")
def add_data(filename):
    fl = os.path.join(os.getcwd(), filename)
    try:
        file = open(fl, "r")
    except FileNotFoundError:
        print(f"ERROR: {fl} does not exist")
    else:
        with file:
            data = json.load(file)
            for row in data:
                # turn date and time json strings into python datetime objects
                row["birthdate"] = datetime.strptime(row["birthdate"], "%Y-%m-%d").date()
                row["last_update"] = datetime.strptime(row["last_update"], '%Y-%m-%d %H:%M:%S')
                profile = models.Profile(**row)
                database.db.session.add(profile)
                try:
                    database.db.session.commit()
                except IntegrityError:
                    print(f"Data for { row['firstname'] } { row['lastname'] } already exists")
                    database.db.session.rollback()
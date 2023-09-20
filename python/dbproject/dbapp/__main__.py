from .interface import cli
from .dbsetup import models

models.db_setup()
cli.main()

from os import environ
from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection

# Loading database credentials from JSON file
def load_db_variables(file_path:str) -> None:
    # Context Manager
    with open (file_path, 'r') as file:

        # Deserialize (JSON to the Python dictionary)
        db_vars:dict = load(file)

        # Close the context
        file.close()

        # Update the enviro dictionary
        environ.update(db_vars)

# Creating SQLAlchemy engine
def create_postgres_engine() -> Engine:
    username = environ.get ('POSTGRES_USER')
    password = environ.get ('POSTGRES_PASSWORD')
    host = environ.get ('POSTGRES_HOST')
    port = environ.get ('POSTGRES_PORT')
    database = environ.get ('POSTGRES_DATABASE')

    engine: Engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')
    return engine
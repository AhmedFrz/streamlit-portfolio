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

        # Clear the db_vars
        db_vars.clear()

# Creating SQLAlchemy engine

def create_postgres_engine(username: str, password: str, host: str, port: str, database: str) -> Engine:
    engine: Engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')
    return engine

# Create the connection
def create_postgres_connection(engine: Engine) -> Connection:
    # Create the connection
    connection: Connection = engine.connect()

    return connection
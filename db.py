from dotenv import dotenv_values
from sqlalchemy import create_engine, MetaData

config = dotenv_values("./.env")

metadata = MetaData()


def db_connect():
    username = config.get("DB_USERNAME")
    password = config.get("DB_PASSWORD")
    dbname = config.get("DB_NAME")

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@localhost:5432/{dbname}",
        echo=False,
        future=True,
    )

    connection = engine.connect()

    return engine, connection


engine, connection = db_connect()
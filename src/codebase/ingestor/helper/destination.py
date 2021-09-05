import os

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

engine = create_engine(URL(
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
))

connection = engine.connect()


def save(df, table):
    # It creates the table if not exists - no need to pre-create
    df.to_sql(table, con=engine, if_exists='replace', index=False)


def close():
    connection.close()
    engine.dispose()

import os

from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine


def open_connection():
    # client.access_secret_version(request={"name": "snowflake_user"})
    # It should retrieve credentials from the GCP Secrets Manager
    # But the current permissions are not permit to access the secrets data.
    engine = create_engine(URL(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    ))

    return engine.connect()


def save(df, table, connection):
    # It creates the table if not exists - no need to pre-create
    df.to_sql(table, con=connection, if_exists='replace', index=False)


def close_connection(connection):
    connection.dispose()

"""This file contains methods for communicating with the database."""

from psycopg2 import connect
from psycopg2.extras import RealDictCursor


def get_db_connection():
    """Returns a connection to the database; all rows are returned as dicts."""
    return connect(
        dbname="clown",
        host="localhost",
        port=5432,
        cursor_factory=RealDictCursor
    )

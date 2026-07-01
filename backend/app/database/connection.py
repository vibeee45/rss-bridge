"""
Database Connection

Creates a PostgreSQL connection.
"""

import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not configured."
    )


def get_connection():
    """
    Returns a PostgreSQL connection.
    """

    return psycopg.connect(DATABASE_URL)
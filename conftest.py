import pytest
from lib.database_connection import DatabaseConnection

@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn
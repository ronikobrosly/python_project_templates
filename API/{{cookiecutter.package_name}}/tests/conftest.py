"""Common fixtures used across unit and integration tests"""

{% if cookiecutter.requires_database_support == 'yes' -%}
from csv import reader
import os
import sqlite3

import pytest
from sqlalchemy import create_engine
{%- endif %}
{% if cookiecutter.requires_database_support == 'no' -%}
from csv import reader
import os

import pytest
{%- endif %}

def json_body_1():
    """
    Test POST request for API. This is payload #1 to test.

    Args: None

    Returns:
        A tuple of JSON body to send to API, and the expected output
    """
    input = {'a': '1', 'b': '2'}
    expected_response = {'answer': '2'}

    return input, expected_response


def json_body_2():
    """
    Test POST request for API. This is payload #2 to test.
    """
    input = {'a': '1', 'b': '2', 'c': '3'}
    expected_response = {'answer': '3'}

    return input, expected_response


def json_body_3():
    """
    Test POST request for API. This is payload #3 to test.
    """
    input = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
    expected_response = {'answer': '4'}

    return input, expected_response


def main_API_inputs_and_outputs():
    return [json_body_1(), json_body_2(), json_body_3()]


{% if cookiecutter.requires_database_support == 'yes' -%}
def load_test_data():
    """Load the test data from the 'tests/integration/fixtures/' folder to
    populate the test database tables.

    Args: None

    Returns:
        A list of tuples containing the test data for the test table.
    """

    fixture_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'integration', 'fixtures')
    table_path = os.path.join(fixture_dir, 'test_table.csv')

    with open(os.path.expanduser(table_path), 'r') as read_obj:
        csv_reader = reader(read_obj)
        fake_table_data = list(map(tuple, csv_reader))

    return fake_table_data


@pytest.fixture(scope="session")
def cursor_fixture():
    """Fixture for the database cursor. Inserts toy data into the table.

    Args: None

    Returns:
        A database connection to SQLite (in memory)
    """

    eng = create_engine("sqlite://")
    cur = eng.connect()
    cur.execute("attach ':memory:' as TEST_SCHEMA")

    # Create an in-memory sqlite table with correct schema and all
    create_table_str = """CREATE TABLE TEST_SCHEMA.test_table (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT
    )
    """
    cur.execute(create_table_str)

    fake_table_data = load_test_data()
    cur.execute('insert into TEST_SCHEMA.test_table (name, address) values (?,?)', fake_table_data)


    class MockCursor():
        def execute(self, raw_sql):
            self.results = cur.execute('SELECT * FROM TEST_SCHEMA.test_table').fetchall()

        def fetchall(self):
            return self.results

        def close(self):
            pass

    return MockCursor()
{%- endif %}

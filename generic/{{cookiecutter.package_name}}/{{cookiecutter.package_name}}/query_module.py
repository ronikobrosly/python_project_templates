{% if cookiecutter.requires_database_support == 'yes' -%}
"""Example query module, contains an example query function"""

import psycopg2


# This is some phony logic just to make fake DB connection and cursor objects
# When doing this for real, delete these empty classes and
# make a real connection object using `psycopg2`
class Connection:
    def close(*args):
        pass


class Cursor:
    def close(*args):
        pass

    def execute(*args):
        pass

    def fetchall(*args):
        pass


CONNECTION = Connection()
CURSOR = Cursor()


def query_module():
    """
    An example of a function to query the DB.

    Args:
        None
    Returns:
        A list of tuples of the query results
    """

    raw_sql = """
        SELECT
          name,
          address
        FROM TEST_SCHEMA.test_table
    """

    try:
        CURSOR.execute(raw_sql)
        result = CURSOR.fetchall()

        CURSOR.close()
        CONNECTION.close()

        return result

    except Exception as ex:
        print(f"Failed to execute query: {ex}")
        CONNECTION.close()
        return None
{%- endif %}

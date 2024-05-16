import sqlite3

from pixiv_sql.lib.illusts import get_illusts_insert
from sqlite.utils import get_sql, upsert_into_table
from sqlite.types import get_types


def create_bookmarked_illusts_table(self):
    """
    This function creates bookmarked_illusts table in the database.

    It connects to the database, executes the SQL script to create the tables,
    commits the changes, and then closes the connection.
    """

    logger = self.logger

    # Connect to the database
    conn = sqlite3.connect(self.database)
    cur = conn.cursor()

    # Get the SQL script
    path = "./src/sql/create/bookmarked_illusts.sql"
    sql_script = get_sql(path)

    # Execute the SQL script
    cur.executescript(sql_script)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    logger.info("[DB] 'bookmarked_illusts' table has been created.")


def insert_illusts(self, illusts: list):
    """
    This function inserts bookmarked illusts into the 'bookmarked_illusts' table in the database.

    Args:
        illusts (list): A list of dictionaries where each dictionary represents a illust.
    """

    # get all types from the database
    types = get_types(self)

    # Get the SQL insert statements for the illusts
    illusts_inserts = get_illusts_insert(illusts, types, self.is_private)

    # Define the name of the table where the bookmarked_illusts will be inserted
    table_name = "bookmarked_illusts"

    # Define the columns of the 'bookmarked_illusts' table
    columns = [
        "id",
        "title",
        "type_id",
        "caption",
        "user_id",
        "create_date",
        "visible",
        "illust_ai_type",
        "illust_book_style",
        "is_private",
    ]

    # Call the function to upsert the bookmarked_illusts into the table
    upsert_into_table(self, table_name, columns, illusts_inserts)

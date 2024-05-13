import sqlite3

from pixiv_sql.lib.tags import get_bookmarks_tags_inserts
from sqlite.insert import insert_into_table
from sqlite.sql import get_sql


def create_illusts_tags_table(self):
    """
    This function creates illusts_tags table in the database.

    It connects to the database, executes the SQL script to create the tables,
    commits the changes, and then closes the connection.
    """

    logger = self.logger

    # Connect to the database
    conn = sqlite3.connect(self.database)
    cur = conn.cursor()

    # Get the SQL script
    path = "./src/sql/create/illusts_tags.sql"
    sql_script = get_sql(path)

    # Execute the SQL script
    cur.executescript(sql_script)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    logger.info("[DB] 'illusts_tags' table has been created.")


def insert_illusts_tags(self, illusts: list):
    """
    This function inserts illusts into the 'illusts_tags' table in the database.

    Args:
        illusts (list): A list of dictionaries where each dictionary represents a illust.
    """

    # Get the SQL insert statements for the illusts_tags
    illusts_tags_inserts = get_bookmarks_tags_inserts(illusts)

    # Define the name of the table where the illusts_tags will be inserted
    table_name = "illusts_tags"

    # Define the columns of the 'illusts_tags' table
    columns = [
        "illust_id",
        "tag_id",
    ]

    # Call the function to insert the illusts_tags into the table
    insert_into_table(self, table_name, columns, illusts_tags_inserts)

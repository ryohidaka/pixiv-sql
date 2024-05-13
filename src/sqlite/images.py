import sqlite3

from sqlite.sql import get_sql


def create_images_table(self):
    """
    This function creates images table in the database.

    It connects to the database, executes the SQL script to create the tables,
    commits the changes, and then closes the connection.
    """

    logger = self.logger

    # Connect to the database
    conn = sqlite3.connect(self.database)
    cur = conn.cursor()

    # Get the SQL script
    path = "./src/sql/create/images.sql"
    sql_script = get_sql(path)

    # Execute the SQL script
    cur.executescript(sql_script)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    logger.info("[DB] 'images' table has been created.")

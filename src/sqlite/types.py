from sqlite.utils import connect_to_database, get_sql


def create_types_table(self):
    """
    This function creates types table in the database.

    It connects to the database, executes the SQL script to create the tables,
    commits the changes, and then closes the connection.
    """

    logger = self.logger

    # Connect to the database
    conn = connect_to_database(self.database)
    cur = conn.cursor()

    # Get the SQL script
    path = "./src/sql/create/types.sql"
    sql_script = get_sql(path)

    # Execute the SQL script
    cur.executescript(sql_script)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    logger.info("[DB] 'types' table has been created.")


def get_types(self) -> list:
    """
    This function is used to get all types from the database.

    Returns:
        list: A list of all types fetched from the database.
    """

    # Connect to the database
    conn = connect_to_database(self.database)
    cur = conn.cursor()

    # Execute the SQL query to fetch all types
    cur.execute("SELECT id, name FROM types")

    # Fetch all rows from the executed SQL query
    rows = cur.fetchall()

    # Return the fetched rows as a list
    return [row for row in rows]

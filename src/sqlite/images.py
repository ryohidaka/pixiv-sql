import sqlite3

from pixiv_sql.lib.images import get_image_inserts
from sqlite.insert import insert_into_table
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


def insert_images(self, illusts: list):
    """
    This function inserts data of images who have created bookmarked illustrations into the 'images' table in the database.

    Args:
        illusts (list): A list of dictionaries, each representing a bookmarked illustration.
    """

    # Get the SQL insert statements for the images
    images_inserts = get_image_inserts(illusts)

    # Define the name of the table where the images will be inserted
    table_name = "images"

    # Define the columns of the 'images' table
    columns = [
        "illust_id",
        "page",
        "is_multiple_page",
        "url",
        "is_square",
        "filename",
    ]

    # Call the function to upsert the images into the table
    insert_into_table(self, table_name, columns, images_inserts)

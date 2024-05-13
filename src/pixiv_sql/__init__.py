import os
from dotenv import load_dotenv
from pixiv_sql.lib.illusts import get_restrict
from pixiv_sql.lib.logger import init_logger
from pixivpy.auth import init_api
from pixivpy.illusts import get_bookmarked_illusts
from sqlite.illusts import create_bookmarked_illusts_table, insert_illusts
from sqlite.illusts_tags import create_illusts_tags_table, insert_illusts_tags
from sqlite.images import create_images_table
from sqlite.tags import create_tags_table, insert_tags
from sqlite.types import create_types_table
from sqlite.users import create_users_table, insert_users

# Load .env file and reflect environment variables.
load_dotenv()


def main() -> int:
    print("Hello from pixiv-sql!")

    user_id = os.environ.get("USER_ID")
    refresh_token = os.environ.get("REFRESH_TOKEN")
    database = os.environ.get("DB")

    app = PixivSQL(user_id, refresh_token, database)
    app.bookmarked_illusts()

    return 0


class PixivSQL:
    def __init__(self, user_id: str, refresh_token: str, database: str):
        """
        The constructor for the PixivSQL class.

        Parameters:
            user_id (str): The user ID for the Pixiv account.
            refresh_token (str): The refresh token for the Pixiv API.
        """

        self.logger = init_logger()

        # Set the user ID, refresh token and database.
        self.user_id = user_id
        self.refresh_token = refresh_token
        self.database = database

        self.logger.info(f"UserID: {self.user_id}")

        # Initialize the API.
        self.api = init_api(self)

    def bookmarked_illusts(self, is_private: bool = False):
        """
        The bookmarked_illusts method for the PixivSQL class.

        This method fetches the bookmarked illusts of the user and inserts them into the database.
        It also creates the necessary tables if they do not exist.

        Parameters:
            is_private (bool): A flag to indicate if the bookmarked illusts are private. Default is False.
        """

        # Get the restrict level based on the is_private flag.
        self.restrict = get_restrict(self, is_private)
        self.is_private = is_private

        # Fetch the bookmarked illusts from the Pixiv API.
        illusts = get_bookmarked_illusts(self)

        # Create the illusts table in the database.
        create_bookmarked_illusts_table(self)

        # Create the types table in the database.
        create_types_table(self)

        # Insert the fetched users into the database.
        insert_illusts(self, illusts)

        # Create the users table in the database.
        create_users_table(self)

        # Insert the fetched users into the database.
        insert_users(self, illusts)

        # Create the tags table in the database.
        create_tags_table(self)

        # Insert the fetched tags into the database.
        insert_tags(self, illusts)

        # Create the illusts_tags table in the database.
        create_illusts_tags_table(self)

        # Insert the fetched illusts_tags pare into the database.
        insert_illusts_tags(self, illusts)

        # Create the images table in the database.
        create_images_table(self)

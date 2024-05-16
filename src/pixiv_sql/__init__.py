import os
from dotenv import load_dotenv
from pixiv_sql.bookmarks import fetch_and_insert_bookmarked_illusts
from pixiv_sql.lib.logger import init_logger
from pixivpy.auth import init_api

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
        fetch_and_insert_bookmarked_illusts(self, is_private)

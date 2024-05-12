import os
from dotenv import load_dotenv
from pixiv_sql.lib.bookmark import get_restrict
from pixiv_sql.lib.logger import init_logger
from pixivpy.auth import init_api
from pixivpy.bookmark import get_bookmarks

# Load .env file and reflect environment variables.
load_dotenv()


def main() -> int:
    print("Hello from pixiv-sql!")

    user_id = os.environ.get("USER_ID")
    refresh_token = os.environ.get("REFRESH_TOKEN")

    app = PixivSQL(user_id, refresh_token)
    app.bookmark()

    return 0


class PixivSQL:
    def __init__(self, user_id: str, refresh_token: str):
        """
        The constructor for the PixivSQL class.

        Parameters:
            user_id (str): The user ID for the Pixiv account.
            refresh_token (str): The refresh token for the Pixiv API.
        """

        self.logger = init_logger()

        # Set the user ID and refresh token.
        self.user_id = user_id
        self.refresh_token = refresh_token

        self.logger.info(f"UserID: {self.user_id}")

        # Initialize the API.
        self.api = init_api(self)

    def bookmark(self, is_private: bool = False):
        """
        The bookmark method for the PixivSQL class.

        This method fetches the bookmarks of the user and inserts them into the database.
        It also creates the necessary tables if they do not exist.

        Parameters:
            is_private (bool): A flag to indicate if the bookmarks are private. Default is False.
        """

        # Get the restrict level based on the is_private flag.
        self.restrict = get_restrict(self, is_private)

        # Fetch the bookmarks from the Pixiv API.
        bookmarks = get_bookmarks(self)
        print(len(bookmarks))

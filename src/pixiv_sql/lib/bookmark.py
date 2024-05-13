from typing import Literal

from pixiv_sql.lib.restrict import get_is_private_value
from pixiv_sql.lib.type import get_type_id


def get_restrict(self, is_private: bool) -> Literal["private", "public"]:
    """
    This method determines the restriction level based on the is_private parameter.

    Parameters:
    is_private (bool): A boolean value that indicates whether the restriction is private.

    Returns:
    str: Returns 'private' if is_private is True, otherwise returns 'public'.
    """

    # Initialize the logger
    logger = self.logger

    # Determine the restriction level
    restrict = "private" if is_private else "public"

    # Log the restriction level
    logger.info(f"Restrict: {restrict}")

    # Return the restriction level
    return restrict


def get_bookmarks_insert(bookmarks, types: list, is_private: bool) -> list[tuple]:
    """
    This function prepares the bookmark data for insertion into the database.

    Args:
        bookmarks (list): A list of dictionaries where each dictionary represents a bookmark.
        types (list): A list of types. Each type is a dictionary that maps a type name to a type id.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the bookmark data to be inserted.
    """

    # Prepare the data for each bookmark
    inserts = []

    for bookmark in bookmarks:
        # Get the type id
        type_id = get_type_id(types, bookmark["type"])

        # Get the is_private flag as int
        is_private_value = get_is_private_value(is_private)

        inserts.append(
            (
                bookmark["id"],
                bookmark["title"],
                type_id,
                bookmark["caption"],
                bookmark["user"]["id"],
                bookmark["create_date"],
                bookmark["visible"],
                bookmark["illust_ai_type"],
                bookmark["illust_book_style"],
                is_private_value,
            )
        )

    return inserts  # Return the prepared data

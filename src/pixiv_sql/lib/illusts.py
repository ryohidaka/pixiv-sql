from typing import Literal

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


def get_illusts_insert(illusts, types: list, is_private: bool) -> list[tuple]:
    """
    This function prepares the bookmarked illusts data for insertion into the database.

    Args:
        illusts (list): A list of dictionaries where each dictionary represents a bookmarked illust.
        types (list): A list of types. Each type is a dictionary that maps a type name to a type id.

    Returns:
        list[tuple]: A list of tuples where each tuple contains the bookmarked illusts data to be inserted.
    """

    # Prepare the data for each illust
    inserts = []

    for illust in illusts:
        # Get the type id
        type_id = get_type_id(types, illust["type"])

        # Get the is_private flag as int
        is_private_value = 1 if is_private else 0

        inserts.append(
            (
                illust["id"],
                illust["title"],
                type_id,
                illust["caption"],
                illust["user"]["id"],
                illust["create_date"],
                illust["visible"],
                illust["illust_ai_type"],
                illust["illust_book_style"],
                is_private_value,
            )
        )

    return inserts  # Return the prepared data

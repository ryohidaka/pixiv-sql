from typing import Literal


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

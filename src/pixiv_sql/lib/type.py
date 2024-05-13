def get_type_id(types: list, type: str) -> int:
    """
    This function returns the id of a given type from a list of types.

    Args:
        types (list): A list of tuples where each tuple consists of an id and a type name.
        type (str): The type name for which the id is to be returned.

    Returns:
        int: The id of the given type if it exists in the list, otherwise None.
    """
    # Iterate over the list of types
    for id, name in types:
        # If the type name matches the given type
        if name == type:
            # Return the corresponding id
            return id
    # If the type does not exist in the list, return None
    return None

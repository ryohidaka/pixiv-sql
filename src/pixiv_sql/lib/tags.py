import hashlib


def get_tags_inserts(illusts: list) -> list:
    """
    Generate a list of tuples containing unique index, name, and translated name for each tag in the illust.

    Parameters:
    illusts (list): A list of bookmarked illusts where each illust is a dictionary containing 'id' and 'tags'.

    Returns:
    inserts (list): A list of tuples where each tuple contains unique index, name, and translated name of a tag.
    """
    all_tags = [tag for item in illusts for tag in item["tags"]]
    tags = [dict(t) for t in set(tuple(d.items()) for d in all_tags)]
    inserts = []
    for tag in tags:
        unique_index = generate_unique_index(tag["name"])
        inserts.append((unique_index, tag["name"], tag["translated_name"]))

    return inserts


def get_bookmarks_tags_inserts(illusts: list) -> list:
    """
    Generate a list of tuples containing illust_id and tag_id in the bookmarked illusts.

    Parameters:
    illusts (list): A list of bookmarked illusts where each illust is a dictionary containing 'id' and 'tags'.

    Returns:
    inserts (list): A list of tuples where each tuple contains illust_id and unique index of a tag.
    """
    inserts = []
    for ilusts in illusts:
        for tag in ilusts["tags"]:
            unique_index = generate_unique_index(tag["name"])
            inserts.append((ilusts["id"], unique_index))

    return inserts


def generate_unique_index(name) -> int:
    """
    Generate a unique index for a given name using SHA-256 hashing.

    Parameters:
    name (str): The name for which to generate a unique index.

    Returns:
    int: The unique index generated from the name.
    """
    return int(hashlib.sha256(name.encode("utf-8")).hexdigest(), 16) % 10**8

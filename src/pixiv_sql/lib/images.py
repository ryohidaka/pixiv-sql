ignore_file_name = "limit_unknown_360.png"


def get_image_inserts(illusts: list) -> list:
    """
    Function to get image inserts from a list of illustrations.

    Args:
        illusts (list): List of illustrations.

    Returns:
        list: List of image inserts.
    """
    inserts = []
    for illust in illusts:
        id = illust["id"]
        is_multiple = 1 if illust["meta_pages"] else 0
        if illust["meta_pages"]:
            inserts.extend(get_multiple_image_inserts(illust, id, is_multiple))
        else:
            insert = get_single_image_insert(illust, id, is_multiple)
            if insert is not None:
                inserts.append(insert)
    return inserts


def get_multiple_image_inserts(illust: dict, id: int, is_multiple: int) -> list:
    """
    Function to get multiple image inserts from an illustration.

    Args:
        illust (dict): Illustration details.
        id (int): Illustration ID.
        is_multiple (int): Flag indicating if the illustration has multiple images.

    Returns:
        list: List of image inserts.
    """
    inserts = []
    for index, page in enumerate(illust["meta_pages"], start=1):
        urls = page["image_urls"]

        original_image_url = urls["original"]
        square_image_url = urls["square_medium"]

        if get_filename(original_image_url) != ignore_file_name:
            inserts.append(create_insert(id, index, is_multiple, original_image_url, 0))
        if get_filename(square_image_url) != ignore_file_name:
            inserts.append(create_insert(id, index, is_multiple, square_image_url, 1))
    return inserts


def get_single_image_insert(illust: dict, id: int, is_multiple: int) -> tuple:
    """
    Function to get a single image insert from an illustration.

    Args:
        illust (dict): Illustration details.
        id (int): Illustration ID.
        is_multiple (int): Flag indicating if the illustration has multiple images.

    Returns:
        tuple: Single image insert.
    """
    original_image_url = illust["meta_single_page"]["original_image_url"]
    if get_filename(original_image_url) == ignore_file_name:
        return None
    return create_insert(id, 1, is_multiple, original_image_url, 0)


def create_insert(
    id: int, index: int, is_multiple: int, url: str, is_square: int
) -> tuple:
    """
    Function to create an image insert.

    Args:
        id (int): Illustration ID.
        index (int): Index of the image.
        is_multiple (int): Flag indicating if the illustration has multiple images.
        url (str): URL of the image.
        is_square (int): Flag indicating if the image is square.

    Returns:
        tuple: Image insert.
    """
    return (id, index, is_multiple, url, is_square, get_filename(url))


def get_filename(url: str) -> str:
    """
    Function to get the filename from a URL.

    Args:
        url (str): URL.

    Returns:
        str: Filename.
    """
    return url.split("/")[-1]

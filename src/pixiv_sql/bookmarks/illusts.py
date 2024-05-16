from pixiv_sql.lib.illusts import get_restrict
from pixivpy.illusts import get_bookmarked_illusts
from sqlite.illusts import create_bookmarked_illusts_table, insert_illusts
from sqlite.illusts_tags import create_illusts_tags_table, insert_illusts_tags
from sqlite.images import create_images_table, insert_images
from sqlite.tags import create_tags_table, insert_tags
from sqlite.types import create_types_table
from sqlite.users import create_users_table, insert_users


def fetch_and_insert_bookmarked_illusts(self, is_private: bool):
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

    # Insert the fetched images into the database.
    insert_images(self, illusts)

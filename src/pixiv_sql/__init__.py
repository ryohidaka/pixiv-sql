from pixiv_sql.lib.logger import init_logger


def main() -> int:
    print("Hello from pixiv-sql!")

    app = PixivSQL()

    return 0


class PixivSQL:
    def __init__(self):
        """
        The constructor for the PixivSQL class.
        """

        self.logger = init_logger()

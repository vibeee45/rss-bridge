from app.parsers.base_parser import BaseParser


class RSSParser(BaseParser):
    """
    Parser for RSS 2.0 feeds.
    """

    DESCRIPTION_FIELDS = [
        "summary",
        "description"
    ]

    DATE_FIELDS = [
        "published",
        "updated"
    ]

    FEED_DESCRIPTION_FIELDS = [
        "description"
    ]

    DEFAULT_LANGUAGE = "en"
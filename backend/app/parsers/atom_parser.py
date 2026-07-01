from app.parsers.base_parser import BaseParser


class AtomParser(BaseParser):
    """
    Parser for Atom feeds.
    """

    DESCRIPTION_FIELDS = [
        "summary",
        "content",
        "description"
    ]

    DATE_FIELDS = [
        "updated",
        "published"
    ]

    FEED_DESCRIPTION_FIELDS = [
        "subtitle",
        "description"
    ]

    DEFAULT_LANGUAGE = "en"
from app.parsers.base_parser import BaseParser


class RDFParser(BaseParser):
    """
    Parser for RDF (RSS 1.0) feeds.
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
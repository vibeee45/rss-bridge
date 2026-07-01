"""
Core Parser

Acts as the application's entry point for parsing XML feeds.
Delegates all parsing responsibilities to the GenericParser.
"""

from app.models.rss_feed import RSSFeed
from app.parsers.generic_parser import GenericParser


class Parser:
    """
    Core parser wrapper.
    """

    def __init__(self):
        self.generic_parser = GenericParser()

    def parse(self, xml: str) -> RSSFeed:
        """
        Parse any supported XML feed into a standardized RSSFeed model.
        """
        return self.generic_parser.parse(xml)


def extract_feed(xml: str) -> RSSFeed:
    """
    Convenience function used throughout the application.
    """

    parser = Parser()

    return parser.parse(xml)
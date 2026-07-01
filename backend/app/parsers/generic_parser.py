import feedparser

from app.models.rss_feed import RSSFeed

from app.parsers.rss_parser import RSSParser
from app.parsers.atom_parser import AtomParser
from app.parsers.rdf_parser import RDFParser
from app.exceptions.parser_exceptions import (
    UnsupportedFeedType
)

class GenericParser:
    """
    Generic parser responsible for detecting the feed type
    and delegating parsing to the appropriate parser.
    """

    def __init__(self):

        self.rss_parser = RSSParser()
        self.atom_parser = AtomParser()
        self.rdf_parser = RDFParser()

    def parse(self, xml: str) -> RSSFeed:
        """
        Detect feed type and return a standardized RSSFeed object.
        """

        feed = feedparser.parse(xml)

        # Feedparser parsing error
        if getattr(feed, "bozo", False):
            print(f"[WARNING] Feed parsing issue: {feed.bozo_exception}")

        version = (
            getattr(feed, "version", "") or ""
        ).lower()

        print(f"[INFO] Feed Version: {version}")

        # -------------------------
        # Atom Feed
        # -------------------------

        if "atom" in version:
            print("[INFO] Using AtomParser")
            return self.atom_parser.parse(feed)

        # -------------------------
        # RDF Feed
        # -------------------------

        if "rdf" in version:
            print("[INFO] Using RDFParser")
            return self.rdf_parser.parse(feed)

        # -------------------------
        # RSS Feed
        # -------------------------

        if "rss" in version or version == "":
            print("[INFO] Using RSSParser")
            return self.rss_parser.parse(feed)

        # -------------------------
        # Unknown Feed Type
        # -------------------------

        raise UnsupportedFeedType(
    f"Unsupported feed type: {version}"
)

def parse_feed(xml: str) -> RSSFeed:
    """
    Convenience function used by the application.
    """

    parser = GenericParser()

    return parser.parse(xml)
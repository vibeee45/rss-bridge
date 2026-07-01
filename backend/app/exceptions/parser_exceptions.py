class ParserError(Exception):
    """Base parser exception."""
    pass


class UnsupportedFeedType(ParserError):
    """Raised when the feed type is unsupported."""
    pass

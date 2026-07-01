class FeedFetchError(Exception):
    """Raised when a feed cannot be downloaded."""
    pass


class InvalidFeedError(Exception):
    """Raised when a feed is invalid."""
    pass

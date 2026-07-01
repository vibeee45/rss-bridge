"""
Feed validator for RSS Bridge.
"""

from typing import List, Tuple

from app.models.rss_feed import RSSFeed


class FeedValidator:
    """
    Validates an RSSFeed before XML generation.
    """

    @staticmethod
    def validate(feed: RSSFeed) -> Tuple[bool, List[str]]:
        """
        Validate an RSSFeed object.

        Returns:
            (is_valid, errors)
        """

        errors = []

        # -------------------------------------
        # Feed Title
        # -------------------------------------

        if not feed.title or not feed.title.strip():

            errors.append("Feed title is required.")

        # -------------------------------------
        # Feed Link
        # -------------------------------------

        if not feed.link or not feed.link.strip():

            errors.append("Feed link is required.")

        # -------------------------------------
        # Feed Description
        # -------------------------------------

        if feed.description is None:

            feed.description = ""

        # -------------------------------------
        # Language
        # -------------------------------------

        if not feed.language:

            feed.language = "en"

        # -------------------------------------
        # Articles
        # -------------------------------------

        if feed.articles is None:

            feed.articles = []

        if len(feed.articles) == 0:

            errors.append("Feed contains no valid articles.")

        return len(errors) == 0, errors
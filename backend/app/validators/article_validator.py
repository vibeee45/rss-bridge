"""
Article validator for RSS Bridge.
"""

from typing import List, Tuple

from app.models.article import Article


class ArticleValidator:
    """
    Validates Article objects.
    """

    @staticmethod
    def validate(article: Article) -> Tuple[bool, List[str]]:

        errors = []

        # -----------------------------------
        # Title
        # -----------------------------------

        if not article.title or not article.title.strip():

            errors.append("Article title is required.")

        # -----------------------------------
        # Link
        # -----------------------------------

        if not article.link or not article.link.strip():

            errors.append("Article link is required.")

        # -----------------------------------
        # Description
        # -----------------------------------

        if not article.description:

            article.description = ""

        # -----------------------------------
        # Image
        # -----------------------------------

        if article.image is None:

            article.image = None

        return len(errors) == 0, errors
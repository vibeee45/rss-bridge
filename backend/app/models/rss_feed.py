from typing import List

from pydantic import BaseModel

from app.models.article import Article


class RSSFeed(BaseModel):
    """
    Represents an entire RSS Feed.
    """

    title: str
    link: str
    description: str
    language: str

    articles: List[Article]
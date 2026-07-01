from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    """
    Represents a single news article.
    """

    title: str
    link: str
    description: str
    pub_date: str
    image: Optional[str] = None
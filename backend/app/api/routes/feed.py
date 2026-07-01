"""
Feed Route

Returns previously converted RSS feeds.
"""

from fastapi import APIRouter
from fastapi.responses import Response

from app.services.feed_service import feed_service

router = APIRouter()


@router.get(
    "/{feed_key}",
    summary="Get Converted Feed",
    description="Returns a previously converted RSS feed."
)
def get_feed(feed_key: str):
    """
    Get converted RSS XML.
    """

    xml = feed_service.get_feed(feed_key)

    return Response(
        content=xml,
        media_type="application/rss+xml"
    )
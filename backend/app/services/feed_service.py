"""
Feed Storage Service

Stores converted RSS feeds in PostgreSQL.
"""

import hashlib

from fastapi import HTTPException

from app.storage.repository import feed_repository


class FeedService:

    def generate_feed_key(
        self,
        source_url: str
    ) -> str:
        """
        Generate unique feed key.
        """

        return hashlib.sha256(
            source_url.encode("utf-8")
        ).hexdigest()[:16]

    def save_feed(
        self,
        source_url: str,
        xml_content: str
    ) -> str:
        """
        Save converted feed.
        """

        feed_key = self.generate_feed_key(source_url)

        feed_repository.save_feed(
            feed_key=feed_key,
            source_url=source_url,
            xml_content=xml_content
        )

        return feed_key

    def get_feed(
        self,
        feed_key: str
    ) -> str:
        """
        Get converted XML.
        """

        xml = feed_repository.get_feed(feed_key)

        if xml is None:

            raise HTTPException(
                status_code=404,
                detail="Feed not found."
            )

        return xml


feed_service = FeedService()
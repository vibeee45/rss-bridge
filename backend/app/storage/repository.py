"""
Feed Repository

Handles all PostgreSQL operations for converted RSS feeds.
"""

from app.database.connection import get_connection


class FeedRepository:
    """
    Repository for storing and retrieving converted RSS feeds.
    """

    def create_table(self):
        """
        Create the converted_feeds table if it does not already exist.
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS converted_feeds (

                        feed_key VARCHAR(64) PRIMARY KEY,

                        source_url TEXT NOT NULL,

                        xml_content TEXT NOT NULL,

                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

                    );
                    """
                )

            conn.commit()

    def save_feed(
        self,
        feed_key: str,
        source_url: str,
        xml_content: str
    ) -> None:
        """
        Save or update a converted RSS feed.
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO converted_feeds
                    (
                        feed_key,
                        source_url,
                        xml_content
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s
                    )
                    ON CONFLICT (feed_key)
                    DO UPDATE SET

                        source_url = EXCLUDED.source_url,
                        xml_content = EXCLUDED.xml_content;
                    """,
                    (
                        feed_key,
                        source_url,
                        xml_content
                    )
                )

            conn.commit()

    def get_feed(
        self,
        feed_key: str
    ) -> str | None:
        """
        Retrieve converted XML using the feed key.
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT xml_content
                    FROM converted_feeds
                    WHERE feed_key = %s;
                    """,
                    (feed_key,)
                )

                row = cursor.fetchone()

                if row is None:
                    return None

                return row[0]

    def feed_exists(
        self,
        feed_key: str
    ) -> bool:
        """
        Check whether a converted feed already exists.
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT EXISTS(
                        SELECT 1
                        FROM converted_feeds
                        WHERE feed_key = %s
                    );
                    """,
                    (feed_key,)
                )

                return cursor.fetchone()[0]

    def delete_feed(
        self,
        feed_key: str
    ) -> bool:
        """
        Delete a converted feed.
        """

        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM converted_feeds
                    WHERE feed_key = %s;
                    """,
                    (feed_key,)
                )

                deleted = cursor.rowcount > 0

            conn.commit()

        return deleted


feed_repository = FeedRepository()
from fastapi import Request

from app.services.feed_service import feed_service
from app.services.fetch_feed import fetch_feed

from app.core.parser import extract_feed

from app.generators.bhaskar_generator import BhaskarGenerator

from app.exceptions.feed_exceptions import (
    FeedFetchError,
    InvalidFeedError
)

from app.exceptions.parser_exceptions import (
    ParserError,
    UnsupportedFeedType
)

from app.exceptions.generator_exceptions import (
    GeneratorError
)


class ConvertService:
    """
    Complete RSS Bridge conversion pipeline.

        URL
          ↓
      Fetch Feed
          ↓
      Parse Feed
          ↓
      Generate XML
          ↓
      Save Feed
          ↓
      Return Feed URL
    """

    def __init__(self):
        self.generator = BhaskarGenerator()

    def convert(
        self,
        url: str,
        request: Request
    ):

        try:

            # Fetch XML from source
            xml = fetch_feed(url)

            # Parse XML into RSSFeed model
            feed = extract_feed(xml)

            # Generate Bhaskar XML
            xml = self.generator.generate(feed)

            # Save converted feed
            feed_key = feed_service.save_feed(
                source_url=url,
                xml_content=xml.decode("utf-8")
                if isinstance(xml, bytes)
                else xml
            )

            # Generate public URL
            base_url = str(request.base_url).rstrip("/")

            feed_url = f"{base_url}/feed/{feed_key}"

            return {
                "success": True,
                "feed_key": feed_key,
                "feed_url": feed_url
            }

        except (
            FeedFetchError,
            InvalidFeedError,
            UnsupportedFeedType,
            ParserError,
            GeneratorError
        ):
            raise

        except Exception as exc:

            raise GeneratorError(
                f"RSS Bridge conversion failed: {exc}"
            ) from exc
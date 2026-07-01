from abc import ABC

from app.models.article import Article
from app.models.rss_feed import RSSFeed

from app.extractors.image_extractor import extract_image

from app.normalizers.html_cleaner import clean_html
from app.normalizers.pubdate import normalize_pub_date

from app.validators.article_validator import ArticleValidator


class BaseParser(ABC):
    """
    Base parser for all feed types.

    Child classes only need to define:

        DESCRIPTION_FIELDS
        DATE_FIELDS
        FEED_DESCRIPTION_FIELDS
    """

    DESCRIPTION_FIELDS = []

    DATE_FIELDS = []

    FEED_DESCRIPTION_FIELDS = []

    DEFAULT_LANGUAGE = "en"

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _get_first(self, data, fields, default=""):
        """
        Return the first non-empty field.
        """

        for field in fields:

            value = data.get(field)

            if value:

                # feedparser content is a list
                if field == "content":

                    if isinstance(value, list):

                        if len(value):

                            return value[0].get("value", default)

                return value

        return default

    # ---------------------------------------------------------
    # Article
    # ---------------------------------------------------------

    def build_article(self, entry):

        article = Article(

            title=entry.get("title", ""),

            link=entry.get("link", ""),

            description=clean_html(

                self._get_first(
                    entry,
                    self.DESCRIPTION_FIELDS
                )

            ),

            pub_date=normalize_pub_date(

                self._get_first(
                    entry,
                    self.DATE_FIELDS
                )

            ),

            image=extract_image(entry)

        )

        return article

    # ---------------------------------------------------------
    # Articles
    # ---------------------------------------------------------

    def build_articles(self, feed):

        articles = []

        for entry in feed.entries:

            article = self.build_article(entry)

            valid, errors = ArticleValidator.validate(article)

            if valid:

                articles.append(article)

        return articles

    # ---------------------------------------------------------
    # Feed
    # ---------------------------------------------------------

    def build_feed(self, feed):

        description = self._get_first(

            feed.feed,

            self.FEED_DESCRIPTION_FIELDS

        )

        rss_feed = RSSFeed(

            title=feed.feed.get(
                "title",
                ""
            ),

            link=feed.feed.get(
                "link",
                ""
            ),

            description=description,

            language=feed.feed.get(
                "language",
                self.DEFAULT_LANGUAGE
            ),

            articles=self.build_articles(feed)

        )

        return rss_feed

    # ---------------------------------------------------------
    # Main
    # ---------------------------------------------------------

    def parse(self, feed):

        return self.build_feed(feed)
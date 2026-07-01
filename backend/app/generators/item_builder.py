from lxml import etree
from lxml.etree import CDATA

from app.models.article import Article
from app.generators.namespaces import (
    MEDIA_NAMESPACE,
    ATOM_NAMESPACE
)


class ItemBuilder:

    def build(self, channel, article: Article):

        item = etree.SubElement(channel, "item")

        # -----------------------
        # Title
        # -----------------------

        title = etree.SubElement(item, "title")
        title.text = CDATA(article.title)

        # -----------------------
        # Link
        # -----------------------

        etree.SubElement(
            item,
            "link"
        ).text = article.link

        # -----------------------
        # GUID
        # -----------------------

        guid = etree.SubElement(
            item,
            "guid"
        )

        guid.set(
            "isPermaLink",
            "true"
        )

        guid.text = article.link

        # -----------------------
        # Atom Link
        # -----------------------

        atom = etree.SubElement(
            item,
            "{%s}link" % ATOM_NAMESPACE
        )

        atom.set(
            "href",
            article.link
        )

        # -----------------------
        # Description
        # -----------------------

        description = etree.SubElement(
            item,
            "description"
        )

        description.text = CDATA(
            article.description
        )

        # -----------------------
        # Publish Date
        # -----------------------

        etree.SubElement(
            item,
            "pubDate"
        ).text = article.pub_date

        # -----------------------
        # Image
        # -----------------------

        if article.image:

            media = etree.SubElement(
                item,
                "{%s}content" % MEDIA_NAMESPACE
            )

            media.set(
                "url",
                article.image
            )

            media.set(
                "type",
                "image/jpeg"
            )
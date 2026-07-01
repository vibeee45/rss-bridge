from datetime import datetime
from email.utils import format_datetime

from lxml import etree

from app.models.rss_feed import RSSFeed
from app.generators.namespaces import ATOM_NAMESPACE


class ChannelBuilder:

    def build(self, channel, feed: RSSFeed):

        etree.SubElement(channel, "title").text = feed.title

        etree.SubElement(channel, "link").text = feed.link

        etree.SubElement(channel, "description").text = feed.description

        etree.SubElement(channel, "language").text = feed.language

        # -----------------------------
        # Atom Self Link
        # -----------------------------

        atom_link = etree.SubElement(
            channel,
            "{%s}link" % ATOM_NAMESPACE
        )

        atom_link.set("href", feed.link)

        atom_link.set("rel", "self")

        atom_link.set(
            "type",
            "application/rss+xml"
        )

        # -----------------------------
        # Dates
        # -----------------------------

        now = format_datetime(datetime.utcnow())

        etree.SubElement(
            channel,
            "lastBuildDate"
        ).text = now

        etree.SubElement(
            channel,
            "pubDate"
        ).text = now

        # -----------------------------
        # Image
        # -----------------------------

        image = etree.SubElement(
            channel,
            "image"
        )

        etree.SubElement(
            image,
            "title"
        ).text = feed.title

        etree.SubElement(
            image,
            "url"
        ).text = ""

        etree.SubElement(
            image,
            "link"
        ).text = feed.link
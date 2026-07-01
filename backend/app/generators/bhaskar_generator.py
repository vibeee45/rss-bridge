from app.generators.xml_builder import XMLBuilder
from app.generators.channel_builder import ChannelBuilder
from app.generators.item_builder import ItemBuilder
from app.models.rss_feed import RSSFeed


class BhaskarGenerator:

    def __init__(self):
        self.builder = XMLBuilder()
        self.channel_builder = ChannelBuilder()
        self.item_builder = ItemBuilder()

    def generate(self, feed: RSSFeed):

        # Create RSS root
        root = self.builder.create_root()

        # Create channel
        channel = self.builder.create_channel(root)

        # Build channel metadata
        self.channel_builder.build(
            channel,
            feed
        )

        # Build all news items
        for article in feed.articles:
            self.item_builder.build(
                channel,
                article
            )

        # Return XML
        return self.builder.tostring(root)
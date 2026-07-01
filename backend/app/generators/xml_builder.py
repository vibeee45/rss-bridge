from lxml import etree

from app.generators.namespaces import (
    MEDIA_NAMESPACE,
    ATOM_NAMESPACE
)


class XMLBuilder:

    def create_root(self):

        nsmap = {
            "media": MEDIA_NAMESPACE,
            "atom": ATOM_NAMESPACE
        }

        return etree.Element(
            "rss",
            version="2.0",
            nsmap=nsmap
        )

    def create_channel(self, root):

        return etree.SubElement(root, "channel")

    def tostring(self, root) -> str:

        return etree.tostring(
            root,
            pretty_print=True,
            encoding="unicode",
            xml_declaration=False
        )
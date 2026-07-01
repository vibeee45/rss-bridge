"""
Category extractor for RSS Bridge.

Extracts article categories from RSS, Atom, and RDF feeds.
"""

from typing import List


def extract_categories(entry) -> List[str]:
    """
    Extract categories from a feed entry.

    Supports:
    - RSS <category>
    - Atom <category term="">
    - Feedparser tags
    """

    categories = []

    # -----------------------------------------
    # Feedparser Tags
    # -----------------------------------------

    tags = entry.get("tags", [])

    for tag in tags:

        category = (
            tag.get("term")
            or tag.get("label")
            or ""
        ).strip()

        if category and category not in categories:

            categories.append(category)

    # -----------------------------------------
    # RSS Category
    # -----------------------------------------

    if entry.get("category"):

        category = entry.get("category").strip()

        if category and category not in categories:

            categories.append(category)

    # -----------------------------------------
    # Categories List
    # -----------------------------------------

    if entry.get("categories"):

        for category in entry.get("categories"):

            category = str(category).strip()

            if category and category not in categories:

                categories.append(category)

    return categories
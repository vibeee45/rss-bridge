"""
Description extractor for RSS Bridge.

Extracts the best available description/content from
RSS, Atom and RDF feeds.
"""

from app.normalizers.html_cleaner import clean_html


def extract_description(entry) -> str:
    """
    Extract the best available article description.

    Priority:
    1. summary
    2. description
    3. content
    4. subtitle
    """

    description = ""

    # -----------------------------------------
    # RSS Summary
    # -----------------------------------------

    if entry.get("summary"):

        description = entry.get("summary")

    # -----------------------------------------
    # RSS Description
    # -----------------------------------------

    elif entry.get("description"):

        description = entry.get("description")

    # -----------------------------------------
    # Atom Content
    # -----------------------------------------

    elif entry.get("content"):

        content = entry.get("content")

        if isinstance(content, list) and content:

            description = content[0].get(
                "value",
                ""
            )

    # -----------------------------------------
    # Subtitle
    # -----------------------------------------

    elif entry.get("subtitle"):

        description = entry.get("subtitle")

    return clean_html(description)
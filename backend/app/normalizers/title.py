"""
Title normalizer for RSS Bridge.
"""

import html
import re


def normalize_title(title: str | None) -> str:
    """
    Normalize an article title.
    """

    if not title:
        return ""

    # Decode HTML entities
    title = html.unescape(title)

    # Remove extra whitespace
    title = re.sub(r"\s+", " ", title)

    return title.strip()
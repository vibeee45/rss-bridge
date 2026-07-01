import re


def extract_image(entry) -> str | None:
    """
    Extract image URL from different RSS formats.
    Priority:
        1. media_content
        2. media_thumbnail
        3. enclosure
        4. HTML description
    """

    # -------------------------
    # media:content
    # -------------------------

    media = entry.get("media_content")

    if media:
        if len(media):
            url = media[0].get("url")

            if url:
                return url

    # -------------------------
    # media:thumbnail
    # -------------------------

    thumb = entry.get("media_thumbnail")

    if thumb:
        if len(thumb):
            url = thumb[0].get("url")

            if url:
                return url

    # -------------------------
    # enclosure
    # -------------------------

    for link in entry.get("links", []):

        if link.get("rel") == "enclosure":

            if link.get("type", "").startswith("image"):

                return link.get("href")

    # -------------------------
    # HTML Description
    # -------------------------

    description = (
        entry.get("summary")
        or entry.get("description")
        or ""
    )

    match = re.search(
        r'<img[^>]+src=["\']([^"\']+)["\']',
        description,
        re.IGNORECASE,
    )

    if match:
        return match.group(1)

    return None
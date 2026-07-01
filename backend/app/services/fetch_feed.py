import requests
from requests.exceptions import RequestException

from app.constants import USER_AGENT, REQUEST_TIMEOUT

from app.exceptions.feed_exceptions import (
    FeedFetchError,
    InvalidFeedError
)


def fetch_feed(url: str) -> str:
    """
    Fetch RSS/XML from a URL.
    """

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8"
    }

    try:

        response = requests.get(
            url=url,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True
        )

        response.raise_for_status()

    except RequestException as exc:

        raise FeedFetchError(
            f"Unable to fetch feed: {url}"
        ) from exc

    if not response.text.strip():

        raise InvalidFeedError(
            "The feed returned an empty response."
        )

    return response.text
import re
from bs4 import BeautifulSoup


def clean_html(text: str) -> str:
    """
    Remove HTML tags and normalize whitespace.
    """

    if not text:
        return ""

    soup = BeautifulSoup(text, "html.parser")

    text = soup.get_text(separator=" ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()
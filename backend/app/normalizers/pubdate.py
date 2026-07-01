from email.utils import format_datetime
from datetime import datetime

from dateutil import parser


def normalize_pub_date(date_str: str) -> str:
    """
    Normalize any valid date string into RFC 822 format.
    """

    if not date_str:
        return ""

    try:
        dt = parser.parse(date_str)

        return format_datetime(dt)

    except Exception:
        return date_str
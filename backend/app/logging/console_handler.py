"""
Console logging handler for RSS Bridge.
"""

import logging

from app.logging.config import LoggingConfig
from app.logging.formatter import ConsoleFormatter


class ConsoleHandler:
    """
    Factory for creating console logging handlers.
    """

    @staticmethod
    def create() -> logging.StreamHandler:
        """
        Create and configure a console handler.
        """

        handler = logging.StreamHandler()

        handler.setLevel(
            LoggingConfig.LOG_LEVEL
        )

        handler.setFormatter(
            ConsoleFormatter()
        )

        return handler
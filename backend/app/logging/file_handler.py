"""
File logging handlers for RSS Bridge.
"""

import logging
from logging.handlers import RotatingFileHandler

from app.logging.config import LoggingConfig
from app.logging.formatter import FileFormatter


class FileHandler:
    """
    Factory responsible for creating rotating file handlers.
    """

    @staticmethod
    def create() -> RotatingFileHandler:
        """
        Create the main application log handler.
        """

        LoggingConfig.initialize()

        handler = RotatingFileHandler(
            filename=LoggingConfig.MAIN_LOG_PATH,
            maxBytes=LoggingConfig.MAX_LOG_SIZE,
            backupCount=LoggingConfig.BACKUP_COUNT,
            encoding="utf-8"
        )

        handler.setLevel(
            LoggingConfig.LOG_LEVEL
        )

        handler.setFormatter(
            FileFormatter()
        )

        return handler

    @staticmethod
    def create_error_handler() -> RotatingFileHandler:
        """
        Create a dedicated error log handler.
        """

        LoggingConfig.initialize()

        handler = RotatingFileHandler(
            filename=LoggingConfig.ERROR_LOG_PATH,
            maxBytes=LoggingConfig.MAX_LOG_SIZE,
            backupCount=LoggingConfig.BACKUP_COUNT,
            encoding="utf-8"
        )

        handler.setLevel(
            logging.ERROR
        )

        handler.setFormatter(
            FileFormatter()
        )

        return handler
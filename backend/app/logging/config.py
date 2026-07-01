"""
Logging configuration for RSS Bridge.
"""

import os
import logging

from app.logging.constants import (
    DEFAULT_LEVEL,
    DEFAULT_FORMAT,
    DATE_FORMAT,
    LOG_DIRECTORY,
    MAIN_LOG_FILE,
    ERROR_LOG_FILE,
    MAX_LOG_SIZE,
    BACKUP_COUNT
)


class LoggingConfig:
    """
    Centralized logging configuration.
    """

    # -----------------------------------------------------
    # General
    # -----------------------------------------------------

    LOG_LEVEL = getattr(
        logging,
        DEFAULT_LEVEL.upper(),
        logging.INFO
    )

    LOG_FORMAT = DEFAULT_FORMAT

    DATE_FORMAT = DATE_FORMAT

    # -----------------------------------------------------
    # Directories
    # -----------------------------------------------------

    LOG_DIRECTORY = LOG_DIRECTORY

    # -----------------------------------------------------
    # Log Files
    # -----------------------------------------------------

    MAIN_LOG_PATH = os.path.join(
        LOG_DIRECTORY,
        MAIN_LOG_FILE
    )

    ERROR_LOG_PATH = os.path.join(
        LOG_DIRECTORY,
        ERROR_LOG_FILE
    )

    # -----------------------------------------------------
    # Rotation
    # -----------------------------------------------------

    MAX_LOG_SIZE = MAX_LOG_SIZE

    BACKUP_COUNT = BACKUP_COUNT

    # -----------------------------------------------------
    # Initialization
    # -----------------------------------------------------

    @classmethod
    def initialize(cls):
        """
        Create required directories.
        """

        os.makedirs(
            cls.LOG_DIRECTORY,
            exist_ok=True
        )
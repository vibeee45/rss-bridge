"""
Custom logging formatters for RSS Bridge.
"""

import json
import logging
from datetime import datetime

from app.logging.config import LoggingConfig
from app.logging.context import get_request_id


class BaseFormatter(logging.Formatter):
    """
    Base formatter that injects the request ID into every log record.
    """

    def inject_context(self, record: logging.LogRecord):

        record.request_id = get_request_id()

        return record


class ConsoleFormatter(BaseFormatter):
    """
    Formatter used for console output.
    """

    def __init__(self):

        super().__init__(
            fmt=LoggingConfig.LOG_FORMAT,
            datefmt=LoggingConfig.DATE_FORMAT
        )

    def format(self, record):

        record = self.inject_context(record)

        return super().format(record)


class FileFormatter(BaseFormatter):
    """
    Formatter used for log files.
    """

    def __init__(self):

        super().__init__(
            fmt=LoggingConfig.LOG_FORMAT,
            datefmt=LoggingConfig.DATE_FORMAT
        )

    def format(self, record):

        record = self.inject_context(record)

        return super().format(record)


class JSONFormatter(BaseFormatter):
    """
    Formatter used for structured JSON logs.
    """

    def format(self, record):

        record = self.inject_context(record)

        log = {

            "timestamp": datetime.utcnow().isoformat(),

            "request_id": record.request_id,

            "level": record.levelname,

            "logger": record.name,

            "module": record.module,

            "function": record.funcName,

            "line": record.lineno,

            "message": record.getMessage()
        }

        if record.exc_info:

            log["exception"] = self.formatException(
                record.exc_info
            )

        return json.dumps(
            log,
            ensure_ascii=False
        )
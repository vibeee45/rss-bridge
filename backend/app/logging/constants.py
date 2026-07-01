"""
Logging constants for RSS Bridge.
"""

# Logger
LOGGER_NAME = "RSSBridge"

# Log Levels
DEFAULT_LEVEL = "INFO"

# Log Format
DEFAULT_FORMAT = (
    "[%(asctime)s] "
    "[%(request_id)s] "
    "%(levelname)s "
    "%(name)s: "
    "%(message)s"
)

# Date Format
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Log Directory
LOG_DIRECTORY = "logs"

# Log Files
MAIN_LOG_FILE = "rss_bridge.log"
ERROR_LOG_FILE = "errors.log"

# Rotation
MAX_LOG_SIZE = 10 * 1024 * 1024      # 10 MB
BACKUP_COUNT = 5
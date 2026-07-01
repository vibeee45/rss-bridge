"""
Logging decorators for RSS Bridge.
"""

import time
from functools import wraps
from typing import Callable, Any

from app.logging.logger import get_logger

logger = get_logger(__name__)


def log_execution_time(func: Callable) -> Callable:
    """
    Log the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        start_time = time.perf_counter()

        try:

            result = func(*args, **kwargs)

            elapsed = (
                time.perf_counter() - start_time
            ) * 1000

            logger.info(
                "%s.%s completed in %.2f ms",
                func.__module__,
                func.__name__,
                elapsed
            )

            return result

        except Exception:

            elapsed = (
                time.perf_counter() - start_time
            ) * 1000

            logger.exception(
                "%s.%s failed after %.2f ms",
                func.__module__,
                func.__name__,
                elapsed
            )

            raise

    return wrapper


def log_method_call(func: Callable) -> Callable:
    """
    Log whenever a function is called.
    """

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        logger.info(
            "Calling %s.%s",
            func.__module__,
            func.__name__
        )

        return func(*args, **kwargs)

    return wrapper


def log_success(message: str):
    """
    Log a custom success message after function execution.
    """

    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)

            logger.info(message)

            return result

        return wrapper

    return decorator


def log_failure(message: str):
    """
    Log a custom error message if a function fails.
    """

    def decorator(func: Callable):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:

                return func(*args, **kwargs)

            except Exception:

                logger.exception(message)

                raise

        return wrapper

    return decorator
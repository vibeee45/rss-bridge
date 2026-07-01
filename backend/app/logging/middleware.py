"""
FastAPI logging middleware for RSS Bridge.
"""

import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.logging.logger import get_logger
from app.logging.context import (
    create_request_id,
    clear_request_id
)


logger = get_logger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that logs every incoming HTTP request.
    """

    async def dispatch(
        self,
        request: Request,
        call_next
    ) -> Response:

        request_id = create_request_id()

        start_time = time.perf_counter()

        try:

            response = await call_next(request)

            elapsed = (
                time.perf_counter() - start_time
            ) * 1000

            response.headers["X-Request-ID"] = request_id

            logger.info(
                "%s %s | Status=%d | Time=%.2f ms",
                request.method,
                request.url.path,
                response.status_code,
                elapsed
            )

            return response

        except Exception:

            elapsed = (
                time.perf_counter() - start_time
            ) * 1000

            logger.exception(
                "%s %s | FAILED | Time=%.2f ms",
                request.method,
                request.url.path,
                elapsed
            )

            raise

        finally:

            clear_request_id()
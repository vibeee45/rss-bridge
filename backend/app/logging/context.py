"""
Request context management for RSS Bridge.
"""

import uuid
from contextvars import ContextVar


class RequestContext:
    """
    Stores request-specific information.
    """

    _request_id: ContextVar[str] = ContextVar(
        "request_id",
        default="-"
    )

    @classmethod
    def create_request_id(cls) -> str:
        """
        Generate and store a new request ID.
        """

        request_id = str(uuid.uuid4())

        cls._request_id.set(request_id)

        return request_id

    @classmethod
    def set_request_id(cls, request_id: str):
        """
        Set the current request ID.
        """

        cls._request_id.set(request_id)

    @classmethod
    def get_request_id(cls) -> str:
        """
        Return the current request ID.
        """

        return cls._request_id.get()

    @classmethod
    def clear_request_id(cls):
        """
        Clear the current request ID.
        """

        cls._request_id.set("-")


# ---------------------------------------------------------
# Convenience Functions
# ---------------------------------------------------------

def create_request_id() -> str:
    return RequestContext.create_request_id()


def get_request_id() -> str:
    return RequestContext.get_request_id()


def set_request_id(request_id: str):
    RequestContext.set_request_id(request_id)


def clear_request_id():
    RequestContext.clear_request_id()
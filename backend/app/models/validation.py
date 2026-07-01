"""
Validation models for RSS Bridge.
"""

from pydantic import BaseModel


class ValidationResult(BaseModel):
    """
    Represents the result of a validation.
    """

    is_valid: bool

    message: str

    errors: list[str] = []
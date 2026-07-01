"""
Language normalizer for RSS Bridge.

Normalizes various language codes into
supported language identifiers.
"""

SUPPORTED_LANGUAGES = {
    # English
    "en": "en",
    "en-us": "en",
    "en-gb": "en",

    # Hindi
    "hi": "hi",
    "hi-in": "hi",

    # Bengali
    "bn": "bn",
    "bn-in": "bn",
    "bn-bd": "bn",

    # Marathi
    "mr": "mr",
    "mr-in": "mr",
}


def normalize_language(language: str | None) -> str:
    """
    Normalize a language code.

    Unknown languages default to English.
    """

    if not language:
        return "en"

    language = language.strip().lower()

    return SUPPORTED_LANGUAGES.get(
        language,
        "en"
    )
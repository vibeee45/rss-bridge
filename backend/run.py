"""
Application entry point for RSS Bridge.
"""

import uvicorn


def main():
    """
    Start the FastAPI application.
    """

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()
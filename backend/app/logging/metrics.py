"""
Application metrics for RSS Bridge.
"""

import time
from threading import Lock


class Metrics:
    """
    In-memory metrics collector.

    Can later be replaced with Prometheus,
    OpenTelemetry or any monitoring system.
    """

    _lock = Lock()

    _requests = 0

    _successful_requests = 0

    _failed_requests = 0

    _rss_feeds = 0

    _atom_feeds = 0

    _rdf_feeds = 0

    _total_response_time = 0.0

    _slowest_request = 0.0

    _parsing_errors = 0

    _generation_errors = 0

    # ---------------------------------------
    # Request Metrics
    # ---------------------------------------

    @classmethod
    def request_started(cls):

        with cls._lock:

            cls._requests += 1

        return time.perf_counter()

    @classmethod
    def request_finished(
        cls,
        start_time: float,
        success: bool = True
    ):

        elapsed = (
            time.perf_counter() - start_time
        ) * 1000

        with cls._lock:

            cls._total_response_time += elapsed

            if elapsed > cls._slowest_request:

                cls._slowest_request = elapsed

            if success:

                cls._successful_requests += 1

            else:

                cls._failed_requests += 1

    # ---------------------------------------
    # Feed Types
    # ---------------------------------------

    @classmethod
    def rss_feed(cls):

        with cls._lock:

            cls._rss_feeds += 1

    @classmethod
    def atom_feed(cls):

        with cls._lock:

            cls._atom_feeds += 1

    @classmethod
    def rdf_feed(cls):

        with cls._lock:

            cls._rdf_feeds += 1

    # ---------------------------------------
    # Errors
    # ---------------------------------------

    @classmethod
    def parser_error(cls):

        with cls._lock:

            cls._parsing_errors += 1

    @classmethod
    def generator_error(cls):

        with cls._lock:

            cls._generation_errors += 1

    # ---------------------------------------
    # Statistics
    # ---------------------------------------

    @classmethod
    def summary(cls):

        with cls._lock:

            average = 0

            if cls._requests:

                average = (
                    cls._total_response_time
                    / cls._requests
                )

            return {

                "requests": cls._requests,

                "successful_requests":
                    cls._successful_requests,

                "failed_requests":
                    cls._failed_requests,

                "rss_feeds":
                    cls._rss_feeds,

                "atom_feeds":
                    cls._atom_feeds,

                "rdf_feeds":
                    cls._rdf_feeds,

                "average_response_time_ms":
                    round(average, 2),

                "slowest_request_ms":
                    round(cls._slowest_request, 2),

                "parsing_errors":
                    cls._parsing_errors,

                "generation_errors":
                    cls._generation_errors
            }

    # ---------------------------------------
    # Reset
    # ---------------------------------------

    @classmethod
    def reset(cls):

        with cls._lock:

            cls._requests = 0
            cls._successful_requests = 0
            cls._failed_requests = 0

            cls._rss_feeds = 0
            cls._atom_feeds = 0
            cls._rdf_feeds = 0

            cls._total_response_time = 0

            cls._slowest_request = 0

            cls._parsing_errors = 0

            cls._generation_errors = 0
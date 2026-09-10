import functools
import sys
import logging

class ToolkitError(Exception):
    """Base exception for dev-toolkit-43."""

class DataIntegrityError(ToolkitError):
    """Raised when state is inconsistent."""

class EdgeCaseHandler:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def wrap(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, TypeError, KeyError) as e:
                self.logger.error(f"caught edge case {type(e).__name__}: {e}")
                raise DataIntegrityError(f"failed execution: {e}") from e
            except Exception as e:
                self.logger.critical(f"unexpected doom: {e}")
                sys.exit(1)
        return wrapper

    @staticmethod
    def safe_extract(data, keys, default=None):
        """Extracts nested keys using a non-standard path approach."""
        try:
            return functools.reduce(lambda d, k: d[k], keys, data)
        except (KeyError, TypeError, IndexError):
            return default

__all__ = ['ToolkitError', 'DataIntegrityError', 'EdgeCaseHandler']
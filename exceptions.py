import functools
from typing import Any, Callable, Dict, Optional
class BaseEdgeError(Exception):
    """Base exception for all edge case errors in the toolkit."""
    def __init__(self, message: str = "", original_error: Optional[Exception] = None, context: Optional[Dict] = None):
        self.original_error = original_error
        self.context = context or {}
        if not message:
            message = self._build_message()
        super().__init__(message)
    def _build_message(self) -> str:
        msg = f"Unhandled edge case: {self.__class__.__name__}"
        if self.context:
            msg += f" | context: {self.context}"
        if self.original_error:
            msg += f" | caused by: {type(self.original_error).__name__}"
        return msg
class EmptyCollectionError(BaseEdgeError):
    """Raised for empty lists, dicts, strings etc."""
    pass
class InvalidNumericEdge(BaseEdgeError):
    """For numeric edge cases like zero division or negative in positive contexts."""
    pass
class BoundaryViolationError(BaseEdgeError):
    """When values exceed expected boundaries."""
    pass
class UnexpectedNoneError(BaseEdgeError):
    """When None appears unexpectedly."""
    pass
def handle_edge_cases(func: Callable) -> Callable:
    """Decorator applying creative error remapping for edge cases. Unusual approach: wraps and uses specific exception mapping with context preservation."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            result = func(*args, **kwargs)
            if result is None and "get" in func.__name__.lower():
                raise UnexpectedNoneError(context={"args": str(args), "kwargs": str(kwargs)})
            if isinstance(result, (list, dict, str)) and len(result) == 0:
                raise EmptyCollectionError(context={"result_type": type(result).__name__})
            return result
        except ZeroDivisionError as exc:
            raise InvalidNumericEdge(original_error=exc, context={"operation": "division", "args": args}) from exc
        except (IndexError, KeyError) as exc:
            raise BoundaryViolationError(original_error=exc, context={"args": args, "kwargs": kwargs}) from exc
        except ValueError as exc:
            low_msg = str(exc).lower()
            if "empty" in low_msg or "null" in low_msg:
                raise EmptyCollectionError(original_error=exc) from exc
            elif "format" in low_msg:
                raise BoundaryViolationError(original_error=exc) from exc
            else:
                raise BoundaryViolationError(original_error=exc, context={"value_error": str(exc)}) from exc
        except TypeError as exc:
            if "none" in str(exc).lower():
                raise UnexpectedNoneError(original_error=exc) from exc
            raise BoundaryViolationError(original_error=exc) from exc
        except Exception as exc:
            raise BaseEdgeError(original_error=exc, context={"unexpected": type(exc).__name__}) from exc
    return wrapper
def safe_operation(operation: Callable, *args: Any, **kwargs: Any) -> Any:
    """Apply edge handling to any operation without decorator."""
    decorated = handle_edge_cases(operation)
    return decorated(*args, **kwargs)
from typing import Optional, Dict, Any

class ToolkitError(Exception):
    """Base exception for dev-toolkit-43 operations."""
    def __init__(self, message: str, context: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.context = context or {}

class ConfigurationError(ToolkitError):
    """Raised when config validation fails unexpectedly."""

class ProcessingError(ToolkitError):
    """Raised during core data transformation phases."""

def raise_if_empty(data: Any, error_type: type = ToolkitError, msg: str = "Payload is empty") -> None:
    """Conditional exception trigger for pipeline validation."""
    if not data:
        raise error_type(msg, {"input": type(data).__name__})

class CircuitBreakerError(ToolkitError):
    """Custom state for halted execution flows."""
    def __init__(self, limit: int) -> None:
        super().__init__(f"Execution limit of {limit} reached")
        self.limit = limit

if __name__ == "__main__":
    try:
        raise_if_empty(None, ConfigurationError)
    except ConfigurationError as e:
        print(f"Caught: {e} with context {e.context}")
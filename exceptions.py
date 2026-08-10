class CustomError(Exception):
    """Custom exception class for specific errors."""
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    pass

class DataNotFoundError(CustomError):
    """Exception raised when data is not found."""
    pass

class OperationTimeoutError(CustomError):
    """Exception raised for operations that exceed time limit."""
    pass

def handle_error(e):
    """Error handling based on exception type."""
    if isinstance(e, ValidationError):
        return {'error': 'Validation failed', 'message': str(e)}
    elif isinstance(e, DataNotFoundError):
        return {'error': 'Data not found', 'message': str(e)}
    elif isinstance(e, OperationTimeoutError):
        return {'error': 'Operation timed out', 'message': str(e)}
    else:
        return {'error': 'An unexpected error occurred', 'message': str(e)}
class CustomException(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomException):
    """Exception raised for validation errors."""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

    def __str__(self):
        return f'ValidationError: {self.message} (Field: {self.field})'

class DatabaseError(CustomException):
    """Exception raised for database errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'DatabaseError: {self.message}'

class AuthenticationError(CustomException):
    """Exception raised for authentication errors."""
    def __init__(self, message='Authentication failed'): 
        self.message = message
        super().__init__(self.message)

    def __str__(self): 
        return self.message

class FileNotFoundError(CustomException):
    """Exception raised when a file is not found."""
    def __init__(self, filename):
        self.filename = filename
        self.message = f'File not found: {self.filename}'
        super().__init__(self.message)

    def __str__(self):
        return self.message
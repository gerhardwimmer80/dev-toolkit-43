class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    def __init__(self, field, message="Invalid value"):
        self.field = field
        self.message = f"{field}: {message}"
        super().__init__(self.message)

class DatabaseConnectionError(CustomError):
    def __init__(self, db_name):
        self.db_name = db_name
        self.message = f"Cannot connect to database: {db_name}"
        super().__init__(self.message)

class UnauthorizedAccessError(CustomError):
    def __init__(self):
        self.message = "You do not have permission to access this resource"
        super().__init__(self.message)
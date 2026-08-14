class CustomError(Exception):
    """Base class for all custom exceptions"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    """Raised when a validation check fails"""
    def __init__(self, field, message):
        self.field = field
        self.message = f'Validation error on {field}: {message}'
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a requested resource is not found"""
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self.message = f'Resource with ID {resource_id} not found'
        super().__init__(self.message)

class PermissionError(CustomError):
    """Raised when access is denied"""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'Access denied to resource: {resource}'
        super().__init__(self.message)

class ConfigurationError(CustomError):
    """Raised when there is a configuration issue"""
    def __init__(self, config_key):
        self.config_key = config_key
        self.message = f'Configuration error with key: {config_key}'
        super().__init__(self.message)
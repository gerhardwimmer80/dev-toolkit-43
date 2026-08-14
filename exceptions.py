class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class DataNotFoundError(CustomError):
    """Exception raised when data is not found."""
    def __init__(self, message="Requested data not found"):  
        self.message = message
        super().__init__(self.message)

class InvalidInputError(CustomError):
    """Exception raised for invalid inputs."""
    def __init__(self, input_value, message="Invalid input provided"):  
        self.input_value = input_value
        self.message = f'{message}: {input_value}'
        super().__init__(self.message)

class ProcessingError(CustomError):
    """Exception raised during processing errors."""
    def __init__(self, message="Error occurred while processing"):  
        self.message = message
        super().__init__(self.message)

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message="Validation failed"):  
        self.message = message
        super().__init__(self.message)

# Example usage of custom exceptions:

def find_data(data_dict, key):
    if key not in data_dict:
        raise DataNotFoundError(f'Key: {key}')
    return data_dict[key]


def validate_number(num):
    if not isinstance(num, (int, float)):
        raise InvalidInputError(num)
    return True

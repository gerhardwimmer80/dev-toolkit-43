import re

def validate_input(data):
    if not isinstance(data, str):
        raise ValueError("Input must be a string")
    if len(data) < 5:
        raise ValueError("Input must be at least 5 characters long")
    if not re.match("^[a-zA-Z0-9]*$", data):
        raise ValueError("Input must only contain alphanumeric characters")
    return True


def main_processing_loop(data):
    try:
        validate_input(data)
        # Process the valid input
        print(f"Processing: {data}")
    except ValueError as e:
        print(f"Validation failed: {e}")
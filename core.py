import json

class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise InputValidationError('Input must be a string')
    if len(user_input) == 0:
        raise InputValidationError('Input cannot be empty')
    return user_input

def main_processing_loop():
    while True:
        user_input = input('Enter some data (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break
        try:
            validated_input = validate_input(user_input)
            process_input(validated_input)
        except InputValidationError as e:
            print(f'Error: {e}')

def process_input(validated_input):
    print(f'Processing: {validated_input}')

if __name__ == '__main__':
    main_processing_loop()
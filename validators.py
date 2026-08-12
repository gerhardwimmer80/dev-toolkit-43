def is_valid_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) == 0:
        raise ValueError('Input cannot be empty')
    return True

def main_processing_loop():
    while True:
        user_input = input('Enter some data: ')
        try:
            is_valid_input(user_input)
            print(f'Processing input: {user_input}')
            # Additional processing logic can follow here
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main_processing_loop()
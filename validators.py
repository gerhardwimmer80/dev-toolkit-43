def validate_input(input_data):
    if not isinstance(input_data, dict):
        raise ValueError("Input must be a dictionary")
    required_keys = ['name', 'age', 'email']
    for key in required_keys:
        if key not in input_data:
            raise ValueError(f'Missing required key: {key}')
        if key == 'age' and not (0 < input_data[key] < 120):
            raise ValueError('Age must be between 1 and 119')
    if '@' not in input_data['email']:
        raise ValueError('Invalid email format')
    return True

if __name__ == '__main__':
    test_input = {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
    try:
        validate_input(test_input)
        print("Input is valid.")
    except ValueError as e:
        print(f'Input validation error: {e}')
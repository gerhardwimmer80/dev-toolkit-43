def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    required_keys = ['name', 'age', 'email']
    for key in required_keys:
        if key not in data:
            raise ValueError(f'Missing required key: {key}')
    if not isinstance(data['name'], str) or len(data['name']) == 0:
        raise ValueError('Name must be a non-empty string')
    if not isinstance(data['age'], int) or data['age'] < 0:
        raise ValueError('Age must be a non-negative integer')
    if '@' not in data['email']:
        raise ValueError('Email must be a valid email address')

if __name__ == '__main__':
    inputs = [
        {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'},
        {'name': '', 'age': 22, 'email': 'jane@example.com'},
    ]
    for input_data in inputs:
        try:
            validate_input(input_data)
            print('Input is valid:', input_data)
        except ValueError as e:
            print('Error:', e)

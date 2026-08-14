def process_data(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    # Additional input validation
    if 'name' not in data or not data['name']:
        raise ValueError('Missing or empty name')
    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise ValueError('Age must be a non-negative integer')
    # Main processing logic
    print(f"Processing data for: {data['name']} with age: {data.get('age', 'N/A')}")

def main():
    users = [
        {'name': 'Alice', 'age': 30},
        {'name': '', 'age': 25},  # This will raise an error
        {'name': 'Bob', 'age': -5},
        {'name': 'Charlie'}
    ]
    for user in users:
        try:
            process_data(user)
        except ValueError as e:
            print(f'Error processing user {user}: {e}')

if __name__ == '__main__':
    main()
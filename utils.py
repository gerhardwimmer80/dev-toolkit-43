def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 'Error: Division by zero is not allowed.'
    except TypeError:
        return 'Error: Inputs must be numbers.'
    else:
        return result


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'Error: File not found.'
    except IOError:
        return 'Error: An I/O error occurred.'


def parse_json(json_string):
    import json
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return 'Error: Invalid JSON format.'
    except TypeError:
        return 'Error: Input must be a string.'


def truncate_string(data, max_length):
    if not isinstance(data, str):
        return 'Error: Input must be a string.'
    return data if len(data) <= max_length else data[:max_length] + '...'


def main():
    print(safe_divide(10, 0))  # Division by zero
    print(read_file('non_existent_file.txt'))  # File not found
    print(parse_json('{invalid_json'))  # Invalid JSON
    print(truncate_string('This is a long string that needs shortening.', 20))  # Truncation

if __name__ == '__main__':
    main()
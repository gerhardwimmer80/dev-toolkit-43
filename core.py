def divide_numbers(numerator, denominator):
    if not isinstance(numerator, (int, float)):
        raise ValueError('Numerator must be a number')
    if not isinstance(denominator, (int, float)):
        raise ValueError('Denominator must be a number')
    if denominator == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return numerator / denominator


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {file_path}')
    except IOError:
        raise IOError('Error reading file')


def process_data(data):
    if not isinstance(data, list):
        raise TypeError('Data must be a list')
    processed = []
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError('Data items must be numbers')
        processed.append(item ** 2)
    return processed


if __name__ == '__main__':
    try:
        result = divide_numbers(10, 0)
        print(result)
    except Exception as e:
        print(f'Error: {e}')
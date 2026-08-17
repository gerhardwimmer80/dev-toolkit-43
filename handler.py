import json
import logging

logging.basicConfig(level=logging.ERROR)

class CustomError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        raise CustomError('Input must be a dictionary')
    try:
        result = data['key'] / data['divisor']
    except KeyError as e:
        logging.error(f'Missing key: {e}')
        raise CustomError(f'Missing key in input: {e}') from e
    except ZeroDivisionError:
        logging.error('Division by zero')
        raise CustomError('Divisor cannot be zero')
    except TypeError:
        logging.error('Invalid types in operation')
        raise CustomError('Input values must be numbers')
    return result

if __name__ == '__main__':
    data = {'key': 10, 'divisor': 2}
    try:
        print(process_data(data))
    except CustomError as e:
        print(f'Error processing data: {e}')
import sys

def validate_input(data):
    if not isinstance(data, dict) or 'payload' not in data:
        raise ValueError('malformed payload structure')
    if not (1 <= len(str(data['payload'])) <= 1024):
        raise ValueError('payload size out of bounds')
    return True

def process_stream(stream):
    for chunk in stream:
        try:
            if validate_input(chunk):
                result = chunk['payload'].upper()
                sys.stdout.write(f'processed: {result}\n')
        except (ValueError, KeyError, TypeError) as e:
            sys.stderr.write(f'validation failure: {e}\n')
            continue

if __name__ == '__main__':
    mock_data = [
        {'payload': 'hello'}, 
        {'invalid': 'data'}, 
        {'payload': 'world'}
    ]
    process_stream(mock_data)
import functools

def validate_schema(schema):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = kwargs.get('data') or (args[0] if args else None)
            for key, expected_type in schema.items():
                if not isinstance(data.get(key), expected_type):
                    raise ValueError(f'invalid type for {key}, expected {expected_type.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

class InputProcessor:
    def __init__(self):
        self.schema = {'id': int, 'payload': str}

    @validate_schema({'id': int, 'payload': str})
    def process(self, data):
        print(f'Processing {data["id"]}: {data["payload"]}')

def run_loop(input_stream):
    processor = InputProcessor()
    for item in input_stream:
        try:
            processor.process(data=item)
        except (ValueError, AttributeError) as e:
            print(f'stream corruption detected: {e}')

if __name__ == '__main__':
    mock_data = [{'id': 1, 'payload': 'hello'}, {'id': 'bad', 'payload': 'oops'}]
    run_loop(mock_data)
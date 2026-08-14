import json
import logging

class ProcessingError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        try:
            if not isinstance(self.data, list):
                raise ProcessingError('Data must be a list.')
            if len(self.data) == 0:
                raise ProcessingError('Data list cannot be empty.')
            processed = [self.process_item(item) for item in self.data]
            return processed
        except ProcessingError as e:
            logging.error(f'Error in processing data: {e}')
            return None
        except Exception as e:
            logging.critical(f'Unexpected error: {e}')
            return None

    def process_item(self, item):
        if not isinstance(item, dict):
            raise ProcessingError(f'Item must be a dictionary, got {type(item).__name__}.')
        # Simulate some processing
        return {k: v for k, v in item.items() if v is not None}

if __name__ == '__main__':
    data = [{'key1': 'value1', 'key2': None}, {'key1': 'value2'}]
    processor = DataProcessor(data)
    result = processor.process_data()
    print(json.dumps(result, indent=2))
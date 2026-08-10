from typing import List, Dict, Any

class DataProcessor:
    def __init__(self, source: str) -> None:
        """
        Initializes the DataProcessor with a source.
        
        :param source: The source of the data to process.
        """
        self.source = source

    def load_data(self) -> List[Dict[str, Any]]:
        """
        Loads data from the specified source.
        
        :return: A list of dictionaries representing the data.
        """
        # In a real implementation, the data would be loaded from a file or database.
        return [
            {'id': 1, 'value': 'example1'},
            {'id': 2, 'value': 'example2'},
        ]

    def process_data(self, data: List[Dict[str, Any]]) -> List[str]:
        """
        Processes the loaded data and extracts values.
        
        :param data: A list of dictionaries containing data.
        :return: A list of processed string values.
        """
        return [item['value'] for item in data if 'value' in item]

    def run(self) -> None:
        """
        Executes the entire data loading and processing workflow.
        """
        data = self.load_data()
        processed_data = self.process_data(data)
        print(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('data_source.txt')
    processor.run()
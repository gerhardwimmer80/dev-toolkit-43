import json
import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_columns(self, **kwargs):
        filtered = self.data
        for key, value in kwargs.items():
            if key in filtered.columns:
                filtered = filtered[filtered[key] == value]
        return filtered

    def to_json(self):
        return self.data.to_json(orient='records')

    def from_json(self, json_str):
        self.data = pd.read_json(json_str)

    def get_summary_statistics(self):
        return self.data.describe(include='all')

if __name__ == '__main__':
    sample_data = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'New York', 'Chicago']
    })
    processor = DataProcessor(sample_data)
    filtered_data = processor.filter_columns(city='New York')
    print(filtered_data)
    print(processor.to_json())
    stats = processor.get_summary_statistics()
    print(stats)
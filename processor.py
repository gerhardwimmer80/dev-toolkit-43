import json
from typing import Any, Dict, Union

class ProcessingError(Exception):
    pass

class DataProcessor:
    def __init__(self, data: Union[str, Dict[str, Any]]) -> None:
        self.data = self.load_data(data)

    def load_data(self, data: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError as e:
                raise ProcessingError(f"Invalid JSON string: {e}")
        elif isinstance(data, dict):
            return data
        else:
            raise ProcessingError("Data must be a JSON string or a dictionary.")

    def process(self) -> Dict[str, Any]:
        try:
            self._validate_data(self.data)
            return self._transform_data(self.data)
        except ProcessingError as e:
            return {"error": str(e)}

    def _validate_data(self, data: Dict[str, Any]) -> None:
        if not isinstance(data, dict):
            raise ProcessingError("Data is not a dictionary.")
        if 'required_key' not in data:
            raise ProcessingError("Missing required key in data.")

    def _transform_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Transformation logic
        return {"transformed_key": data['required_key'] * 2}

if __name__ == '__main__':
    processor = DataProcessor({'required_key': 5})
    result = processor.process()
    print(result)  

import json
from typing import Any, Dict, List, Union

def read_json(file_path: str) -> Union[Dict[str, Any], None]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error reading {file_path}: {str(e)}')
        return None

def write_json(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except IOError as e:
        print(f'Error writing to {file_path}: {str(e)}')
        return False

def flatten_list(nested_list: List[Union[int, List]]) -> List[int]:
    if not isinstance(nested_list, list):
        return [nested_list]  # base case
    flattened = []
    for item in nested_list:
        flattened.extend(flatten_list(item))
    return flattened

def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Example usage
if __name__ == '__main__':
    print(read_json('data.json'))  # Implementing example usage

import json
from typing import Any, Dict

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """Save data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries recursively."""
    result = dict(dict1)  # Start with the first dictionary
    for key, value in dict2.items():
        if (key in result and 
            isinstance(result[key], dict) and 
            isinstance(value, dict)):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary."""
    items = []
    for key, value in nested_dict.items():
        new_key = f'{parent_key}{sep}{key}' if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep = sep).items())
        else:
            items.append((new_key, value))
    return dict(items)
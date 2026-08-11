import json
from typing import Any, Dict, List, Tuple


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    processed = []
    for entry in data:
        new_entry = {"id": entry.get('id'), "value": entry.get('value', 0) * 2}
        processed.append(new_entry)
    return processed


def save_to_file(filename: str, data: List[Dict[str, Any]]) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_from_file(filename: str) -> List[Dict[str, Any]]:
    with open(filename, 'r') as file:
        return json.load(file)


def validate_data(data: List[Dict[str, Any]]) -> bool:
    if not data:
        return False
    for entry in data:
        if not isinstance(entry, dict) or 'id' not in entry:
            return False
    return True


def summarize_data(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_value = sum(entry.get('value', 0) for entry in data)
    count = len(data)
    return {"total": total_value, "count": count}
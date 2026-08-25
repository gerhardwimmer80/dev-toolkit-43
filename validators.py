import re
from dataclasses import dataclass
from typing import List, Dict, Any, Callable

@dataclass
class ValidationRule:
    field: str
    validator: Callable[[Any], bool]
    error_msg: str = "Invalid input"

def is_not_empty(value: Any) -> bool:
    if value is None:
        return False
    return bool(str(value).strip())

def is_valid_email(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, value) is not None

def is_positive_number(value: Any) -> bool:
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        return False

def validate_data(data: Dict[str, Any], rules: List[ValidationRule]) -> List[str]:
    errors = []
    for rule in rules:
        if rule.field not in data:
            errors.append(f"Missing field: {rule.field}")
            continue
        value = data[rule.field]
        if not rule.validator(value):
            errors.append(rule.error_msg)
    return errors

def process_inputs(inputs: List[Dict[str, Any]]) -> None:
    rules = [
        ValidationRule("user_id", is_positive_number, "User ID must be positive number"),
        ValidationRule("email", is_valid_email, "Email format invalid"),
        ValidationRule("name", is_not_empty, "Name cannot be empty")
    ]
    for idx, item in enumerate(inputs):
        errors = validate_data(item, rules)
        if not errors:
            processed = dict(item)
            print(f"Processed item {idx}: {processed}")
        else:
            print(f"Validation failed for item {idx}: {errors}")

if __name__ == "__main__":
    sample_inputs = [
        {"user_id": 42, "email": "test@example.com", "name": "Alice"},
        {"user_id": -1, "email": "invalid", "name": ""},
        {"user_id": 100, "email": "valid@test.org", "name": "Bob"}
    ]
    process_inputs(sample_inputs)
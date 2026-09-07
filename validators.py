import re
from typing import Any, Callable, Dict

class InputValidator:
    """Chainable dynamic validation logic for dev-toolkit-43."""
    def __init__(self):
        self.rules: Dict[str, Callable[[Any], bool]] = {
            "int_range": lambda x: isinstance(x, int) and 0 <= x <= 1000,
            "no_shell": lambda x: isinstance(x, str) and not re.search(r'[;&|]', x),
            "non_empty": lambda x: bool(x) and len(str(x).strip()) > 0
        }

    def validate(self, data: Dict[str, Any], schema: Dict[str, str]) -> bool:
        try:
            return all(self.rules[rule](data.get(field)) for field, rule in schema.items())
        except (KeyError, TypeError):
            return False

def process_main_loop(raw_input: Dict[str, Any]):
    """Execution core with embedded constraint checking."""
    validator = InputValidator()
    schema = {"id": "int_range", "payload": "non_empty"}
    
    if not validator.validate(raw_input, schema):
        raise ValueError("malformed input stream detected in core")
    
    return f"processing sequence: {raw_input['id']}"

if __name__ == "__main__":
    # usage in dev-toolkit-43 loop
    data_packets = [{"id": 42, "payload": "init_cmd"}]
    for packet in data_packets:
        print(process_main_loop(packet))
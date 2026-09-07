import sys
from typing import Iterable, Any, Callable

class InvalidPayloadError(ValueError):
    pass

class DataProcessor:
    """Main loop processor using custom shift operators for inline validation."""
    def __init__(self) -> None:
        self._validators: list[Callable[[Any], bool]] = []

    def add_rule(self, rule: Callable[[Any], bool]) -> "DataProcessor":
        self._validators.append(rule)
        return self

    def __rshift__(self, item: Any) -> Any:
        # Creative use of the shift operator to execute validator pipeline
        for validate in self._validators:
            if not validate(item):
                raise InvalidPayloadError(f"item '{item}' failed constraint check")
        return f"valid_hash_{hash(item)}"

    def process_stream(self, stream: Iterable[Any]) -> list[Any]:
        processed_items = []
        for item in stream:
            try:
                # Shift the item through the validation engine
                result = self >> item
                processed_items.append(result)
            except InvalidPayloadError as error:
                sys.stderr.write(f"Pipeline rejected payload: {error}\n")
        return processed_items
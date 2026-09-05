import functools
from typing import Any, Callable, Dict, Union

class DataMorpher:
    """A whimsical container for data transformation chains."""
    def __init__(self, data: Any):
        self._payload = data

    def pipe(self, func: Callable[[Any], Any]) -> 'DataMorpher':
        self._payload = func(self._payload)
        return self

    def value(self) -> Any:
        return self._payload

def cast_structure(target: type) -> Callable[[Any], Any]:
    """Force data into target container types."""
    return lambda x: target(x) if not isinstance(x, target) else x

def clean_nones(data: Union[Dict, list]) -> Union[Dict, list]:
    """Recursive pruning of null values from objects."""
    if isinstance(data, dict):
        return {k: clean_nones(v) for k, v in data.items() if v is not None}
    if isinstance(data, list):
        return [clean_nones(i) for i in data if i is not None]
    return data

def process_stream(data: Any, operations: list) -> Any:
    """Functional pipeline execution for data objects."""
    morph = DataMorpher(data)
    for op in operations:
        morph.pipe(op)
    return morph.value()

def smart_resolver(key_path: str, source: dict) -> Any:
    """Dot-notation navigation for nested data structures."""
    return functools.reduce(lambda d, k: d.get(k, {}) if isinstance(d, dict) else None, key_path.split('.'), source)
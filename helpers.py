import functools
from typing import Any, Callable, Iterable, List, Dict, Optional


class Pipe:
    """A wrapper enabling functional pipeline syntax using the >> operator."""
    def __init__(self, value: Any):
        self.value = value

    def __rshift__(self, func: Callable) -> "Pipe":
        if callable(func):
            return Pipe(func(self.value))
        raise TypeError(f"Object {func} is not callable")

    def __call__(self) -> Any:
        return self.value

    def __repr__(self) -> str:
        return f"Pipe({self.value!r})"


def deep_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = ".") -> Any:
    """Retrieve nested dictionary values using a dot-separated key path."""
    keys = path.split(sep)
    curr = data
    for k in keys:
        if isinstance(curr, dict) and k in curr:
            curr = curr[k]
        else:
            return default
    return curr


def chunkify(iterable: Iterable[Any], size: int) -> List[List[Any]]:
    """Split an iterable into fixed-size chunks using an iterator generator."""
    it = iter(iterable)
    return list(iter(lambda: [val for _, val in zip(range(size), it)], []))


def flatten(nested_list: List[Any]) -> List[Any]:
    """Recursively flatten arbitrarily nested lists or tuples."""
    result = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def coalesce(*args: Any) -> Any:
    """Return the first non-None argument passed in."""
    return next((arg for arg in args if arg is not None), None)

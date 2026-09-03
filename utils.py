from typing import Any, Callable, Dict, List, TypeVar, Union

T = TypeVar('T')

def compose_pipelines(funcs: List[Callable[[Any], Any]]) -> Callable[[Any], Any]:
    """Chain a sequence of functions into a single pipeline operation."""
    def pipeline(data: Any) -> Any:
        for func in funcs:
            data = func(data)
        return data
    return pipeline

def map_keys(data: Dict[str, Any], mapper: Dict[str, str]) -> Dict[str, Any]:
    """Transform dictionary keys based on a provided translation mapping."""
    return {mapper.get(k, k): v for k, v in data.items()}

def safe_get(target: Any, keys: str, default: Any = None) -> Any:
    """Traverse nested structures using dot-notation key strings."""
    parts = keys.split('.')
    current = target
    try:
        for part in parts:
            if isinstance(current, dict):
                current = current[part]
            else:
                current = getattr(current, part)
        return current if current is not None else default
    except (KeyError, AttributeError, TypeError):
        return default

def chunk_stream(iterable: List[T], size: int) -> List[List[T]]:
    """Divide a linear sequence into smaller, manageable chunks."""
    return [iterable[i : i + size] for i in range(0, len(iterable), size)]

if __name__ == '__main__':
    data_sample = {'user': {'id': 43, 'name': 'dev'}}
    print(safe_get(data_sample, 'user.name'))
import functools
from typing import Any, Callable, Dict, Optional

class EdgeCaseException(Exception):
    """Custom base for edge case errors."""
    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.original_error = original_error

def creative_error_handler(default_return: Any = None, verbose: bool = False) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except ZeroDivisionError:
                if verbose:
                    print("Unusual handling: zero division fallback")
                return default_return
            except IndexError:
                if verbose:
                    print("Unusual handling: index error creative fallback")
                if args and isinstance(args[0], (list, tuple)) and len(args[0]) > 0:
                    return args[0][-1]
                return default_return
            except KeyError:
                if verbose:
                    print("Unusual handling: key error default")
                return default_return
            except (TypeError, ValueError):
                if verbose:
                    print("Unusual handling: type value edge case")
                return 0 if isinstance(default_return, (int, float)) else default_return
            except Exception as e:
                if verbose:
                    print(f"General edge case: {type(e).__name__}")
                raise EdgeCaseException(f"Edge case in {func.__name__}") from e
        return wrapper
    return decorator

@creative_error_handler(default_return=0, verbose=True)
def safe_divide(a: float, b: float) -> float:
    return a / b

@creative_error_handler(default_return=None, verbose=True)
def safe_access(container: Any, key: Any) -> Any:
    if isinstance(container, (list, tuple)):
        return container[key]
    elif isinstance(container, dict):
        return container[key]
    return container

class EdgeCaseHandler:
    def __init__(self):
        self.cases_handled: Dict[str, int] = {}
    def handle_operation(self, op: Callable, *args: Any, **kwargs: Any) -> Any:
        try:
            return op(*args, **kwargs)
        except Exception as e:
            case = type(e).__name__
            self.cases_handled[case] = self.cases_handled.get(case, 0) + 1
            if isinstance(e, ZeroDivisionError):
                return 0
            elif isinstance(e, (IndexError, KeyError)):
                return None
            return "edge_case_recovered"
    def get_handled_count(self) -> Dict[str, int]:
        return self.cases_handled

def handle_edge_data(data: Any) -> Any:
    if not data:
        return "empty_edge_handled"
    try:
        return len(data) if hasattr(data, '__len__') else data
    except:
        return "error_edge_handled"
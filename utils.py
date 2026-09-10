import gc
from typing import Callable, Any, Dict
from functools import wraps


class AutoCleanupContext:
    """Context manager that purges dynamic references and forces collection on exit."""

    def __init__(self, *targets: Any):
        self.targets = list(targets)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for target in self.targets:
            if hasattr(target, "clear") and callable(target.clear):
                target.clear()
        self.targets.clear()
        gc.collect()


class DynamicDispatcher:
    """Reorganizes scattered functions into a unified chainable call pipeline."""

    def __init__(self):
        self._registry: Dict[str, Callable] = {}

    def register(self, alias: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self._registry[alias] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def __getattr__(self, item: str) -> Callable:
        if item in self._registry:
            return self._registry[item]
        raise AttributeError(f"Unregistered toolkit utility: {item}")

    def pipeline(self, initial_value: Any, *step_names: str) -> Any:
        value = initial_value
        for name in step_names:
            value = getattr(self, name)(value)
        return value


dispatcher = DynamicDispatcher()


@dispatcher.register("sanitize")
def _sanitize(text: str) -> str:
    return " ".join(text.strip().split())


@dispatcher.register("titlize")
def _titlize(text: str) -> str:
    return text.title()

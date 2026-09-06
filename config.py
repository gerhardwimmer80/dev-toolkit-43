import json
import os
from collections import ChainMap
from typing import Any, Dict


class DynamicConfigProxy:
    """A dynamic configuration proxy supporting nested attribute access and default fallbacks."""

    def __init__(self, *sources: Dict[str, Any], defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}
        self._data = ChainMap(*sources, self._defaults)

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        current = self._data
        for k in keys:
            if isinstance(current, (dict, ChainMap, DynamicConfigProxy)) and k in current:
                current = current[k]
            else:
                return default
        return current

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            val = self._data[name]
            if isinstance(val, dict):
                return DynamicConfigProxy(val, defaults=self._defaults.get(name, {}))
            return val
        raise AttributeError(f"Configuration key '{name}' not found")

    def __getitem__(self, item: str) -> Any:
        return self.get(item)


def load_config(filepath: str = None, defaults: Dict[str, Any] = None) -> DynamicConfigProxy:
    """Loads configuration merging environment, file data, and defaults."""
    default_dict = defaults or {
        "app": {"name": "dev-toolkit", "version": "1.0.0", "debug": False},
        "server": {"host": "127.0.0.1", "port": 8080},
        "logging": {"level": "INFO"}
    }

    file_config = {}
    if filepath and os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            file_config = json.load(f)

    env_config = {}
    for key, value in os.environ.items():
        if key.startswith("APP_"):
            parts = key.lower().split("_")[1:]
            curr = env_config
            for part in parts[:-1]:
                curr = curr.setdefault(part, {})
            if value.isdigit():
                parsed_val = int(value)
            elif value.lower() in ("true", "false"):
                parsed_val = value.lower() == "true"
            else:
                parsed_val = value
            curr[parts[-1]] = parsed_val

    return DynamicConfigProxy(env_config, file_config, defaults=default_dict)

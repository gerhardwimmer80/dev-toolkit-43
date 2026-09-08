import os
import json
from typing import Any, Dict

class Config:
    """A dynamic configuration loader with typed environment overrides."""
    def __init__(self, defaults: Dict[str, Any], prefix: str = "APP_"):
        self._defaults = defaults
        self._prefix = prefix
        self._file_data: Dict[str, Any] = {}

    def load(self, filepath: str) -> "Config":
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    self._file_data = json.load(f)
                except json.JSONDecodeError:
                    self._file_data = {}
        return self

    def __getattr__(self, name: str) -> Any:
        env_key = f"{self._prefix}{name.upper()}"
        default_val = self._defaults.get(name)

        if env_key in os.environ:
            env_val = os.environ[env_key]
            if default_val is not None:
                target_type = type(default_val)
                if target_type is bool:
                    return env_val.lower() in ("true", "1", "yes", "on")
                try:
                    return target_type(env_val)
                except (ValueError, TypeError):
                    return env_val
            return env_val

        if name in self._file_data:
            return self._file_data[name]

        if name in self._defaults:
            return self._defaults[name]

        raise AttributeError(f"Configuration key {name!r} is undefined")

    def __getitem__(self, key: str) -> Any:
        try:
            return getattr(self, key)
        except AttributeError as err:
            raise KeyError(key) from err
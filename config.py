import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], config_path: str = "config.json"):
        self.defaults = defaults
        self.path = config_path
        self.settings = self._load()

    def _load(self) -> Dict[str, Any]:
        if not os.path.exists(self.path):
            return self.defaults
        try:
            with open(self.path, "r") as f:
                loaded = json.load(f)
            return {**self.defaults, **loaded}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    def __getattr__(self, name: str) -> Any:
        if name in self.settings:
            return self.settings[name]
        raise AttributeError(f"Key '{name}' not found in configuration")

    def __getitem__(self, key: str) -> Any:
        return self.settings[key]

    def update(self, **kwargs):
        self.settings.update(kwargs)
        with open(self.path, "w") as f:
            json.dump(self.settings, f, indent=4)

def get_config(defaults: Dict[str, Any]) -> ConfigLoader:
    return ConfigLoader(defaults)
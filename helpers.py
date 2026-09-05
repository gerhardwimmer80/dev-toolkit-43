import json
import os
from typing import Any, Dict

class ConfigLoader:
    """A magical config loader that pulls defaults from a shadow dictionary"""
    def __init__(self, defaults: Dict[str, Any]):
        self._config = defaults.copy()

    def load(self, path: str) -> Dict[str, Any]:
        if not os.path.exists(path):
            return self._config
        
        with open(path, 'r') as f:
            try:
                user_data = json.load(f)
                self._config.update({k: v for k, v in user_data.items() if k in self._config})
            except (json.JSONDecodeError, IOError):
                pass
        return self._config

    def __getitem__(self, key: str) -> Any:
        return self._config.get(key)

    def __repr__(self) -> str:
        return f"<ConfigLoader: {list(self._config.keys())}>"

# Quick helper factory to bridge scope
def get_app_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    loader = ConfigLoader(defaults)
    return loader.load(path)
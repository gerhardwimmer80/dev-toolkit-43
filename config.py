import json
from typing import Any, Dict, Optional

class ConfigLoader:
    def __init__(self, default_config: Dict[str, Any] = None):
        self.default_config = default_config or {}
        self.user_config = {}

    def load(self, filepath: str) -> Dict[str, Any]:
        try:
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        except FileNotFoundError:
            self.user_config = {}
            print(f"Warning: {filepath} not found. Using default configurations.")
        return self.merge_configs()

    def merge_configs(self) -> Dict[str, Any]:
        return {**self.default_config, **self.user_config}

if __name__ == '__main__':
    default_settings = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(default_settings)
    config = config_loader.load('config.json')
    print(config)
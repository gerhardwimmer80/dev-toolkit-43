import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def update_config(self, custom_config_path: str):
        if os.path.exists(custom_config_path):
            with open(custom_config_path, 'r') as file:
                custom_config = json.load(file)
                self.config.update(custom_config)

    def get(self, key, fallback=None):
        return self.config.get(key, fallback)

# Example usage:
# loader = ConfigLoader('default_config.json')
# loader.update_config('custom_config.json')
# print(loader.get('some_key', 'default_value'))
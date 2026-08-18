import json
import os

class ConfigLoader:
    def __init__(self, default_config: dict = None):
        self.default_config = default_config or {}
        self.loaded_config = self.default_config.copy()

    def load_from_file(self, filepath: str):
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r') as file:
            file_config = json.load(file)
            self.merge_config(file_config)

    def merge_config(self, new_config: dict):
        for key, value in new_config.items():
            if isinstance(value, dict) and key in self.loaded_config:
                self.loaded_config[key] = self.merge_dicts(self.loaded_config[key], value)
            else:
                self.loaded_config[key] = value

    def merge_dicts(self, dict1: dict, dict2: dict) -> dict:
        for key, value in dict2.items():
            if key in dict1 and isinstance(dict1[key], dict):
                dict1[key] = self.merge_dicts(dict1[key], value)
            else:
                dict1[key] = value
        return dict1

    def get_config(self):
        return self.loaded_config

# Example usage:
# default_config = {'app_name': 'MyApp', 'version': '1.0', 'settings': {}}  
# config_loader = ConfigLoader(default_config)
# config_loader.load_from_file('config.json')  
# config = config_loader.get_config()
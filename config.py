import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.user_config = {}

    def load_from_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        else:
            self.user_config = {}

    def get(self, key):
        return self.user_config.get(key, self.default_config.get(key))

    def get_all(self):
        combined_config = self.default_config.copy()
        combined_config.update(self.user_config)
        return combined_config

# Example usage:
# default_config = {'host': 'localhost', 'port': 8080}
# config_loader = ConfigLoader(default_config)
# config_loader.load_from_file('config.json')
# print(config_loader.get_all())
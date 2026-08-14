import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json'):
        self.default_config_path = default_config_path
        self.user_config_path = 'user_config.json'
        self.config = self.load_config()

    def load_config(self):
        config_data = self.load_default_config()
        user_data = self.load_user_config()
        return {**config_data, **user_data}

    def load_default_config(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as file:
                return json.load(file)
        return {}

    def load_user_config(self):
        if os.path.exists(self.user_config_path):
            with open(self.user_config_path, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(self.user_config_path, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example Usage:
# config_loader = ConfigLoader()
# print(config_loader.get('setting_key', 'default_value'))
# config_loader.set('new_setting', 'new_value')

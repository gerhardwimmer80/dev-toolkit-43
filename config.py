import json
import os

class ConfigLoader:
    def __init__(self, default_settings=None, env_file='.env'):
        self.default_settings = default_settings or {}
        self.env_file = env_file
        self.loaded_settings = {}
        self.load_env_variables()

    def load_env_variables(self):
        if os.path.exists(self.env_file):
            with open(self.env_file) as f:
                for line in f.readlines():
                    key, value = line.strip().split('=', 1)
                    self.loaded_settings[key] = value

    def get(self, key, default=None):
        return self.loaded_settings.get(key, self.default_settings.get(key, default))

    def load_json_config(self, json_file):
        if os.path.exists(json_file):
            with open(json_file, 'r') as f:
                json_config = json.load(f)
                self.loaded_settings.update(json_config)

    def get_all_settings(self):
        return {**self.default_settings, **self.loaded_settings}

# Example usage:
# default_config = {'APP_MODE': 'development', 'DEBUG': True}
# config_loader = ConfigLoader(default_settings=default_config)
# config_loader.load_json_config('config.json')
# app_mode = config_loader.get('APP_MODE')
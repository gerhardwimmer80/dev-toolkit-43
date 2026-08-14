import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filepath):
            raise ConfigError(f'Config file not found: {self.filepath}')
        try:
            with open(self.filepath, 'r') as file:
                config = json.load(file)
                if not isinstance(config, dict):
                    raise ConfigError('Config file must contain a dictionary')
                return config
        except json.JSONDecodeError as e:
            raise ConfigError(f'Error decoding JSON: {str(e)}')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        if key not in self.config_data:
            if default is None:
                raise ConfigError(f'Key {key} not found in config')
            return default
        return self.config_data[key]

    def set(self, key, value):
        self.config_data[key] = value
        self.save_config()

    def save_config(self):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving config: {str(e)}')

import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self):
        with open(self.default_config_path) as f:
            return json.load(f)

    def load_from_env(self, env_prefix):
        for key in os.environ:
            if key.startswith(env_prefix):
                config_key = key[len(env_prefix):].lower()
                self.config[config_key] = os.environ[key]

    def get_config(self):
        return self.config

if __name__ == '__main__':
    default_config_file = 'default_config.json'
    loader = ConfigLoader(default_config_file)
    loader.load_from_env('MYAPP_')
    final_config = loader.get_config()
    print(final_config)
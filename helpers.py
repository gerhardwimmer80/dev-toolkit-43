import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.load_config()

    def load_config(self):
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            return self.merge_configs(self.default_config, user_config)
        return self.default_config

    def merge_configs(self, default, user):
        merged = default.copy()
        merged.update(user)
        return merged

    def get(self, key):
        return self.config.get(key)

# Example usage:
def main():
    default_settings = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config_loader = ConfigLoader(default_settings)
    print(config_loader.get('host'))

if __name__ == '__main__':
    main()
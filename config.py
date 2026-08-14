import json
import os

class ConfigLoader:
    def __init__(self, default_config, user_config_path):
        self.default_config = default_config
        self.user_config_path = user_config_path
        self.config = self.load_configuration()

    def load_configuration(self):
        config = self.default_config.copy()
        if os.path.exists(self.user_config_path):
            with open(self.user_config_path, 'r') as f:
                user_config = json.load(f)
                self.update_config(config, user_config)
        return config

    def update_config(self, config, user_config):
        for key, value in user_config.items():
            if isinstance(value, dict) and key in config:
                config[key].update(value)
            else:
                config[key] = value

# Example of default configuration
def get_default_config():
    return {
        'setting_1': 'default_value_1',
        'setting_2': {
            'sub_setting_1': 'default_sub_value_1',
            'sub_setting_2': 'default_sub_value_2'
        },
        'setting_3': 10
    }

if __name__ == '__main__':
    default_config = get_default_config()
    user_config_path = 'user_config.json'
    config_loader = ConfigLoader(default_config, user_config_path)
    print(config_loader.config)
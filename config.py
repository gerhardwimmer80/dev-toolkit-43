import os
from typing import Any, Dict

class AppConfig:
    def __init__(self) -> None:
        self._settings: Dict[str, Any] = {
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "version": "43.0.1",
            "registry": "dev-toolkit-43"
        }

    def __getitem__(self, key: str) -> Any:
        return self._settings.get(key)

    @classmethod
    def load_environment(cls) -> 'AppConfig':
        instance = cls()
        for key, value in os.environ.items():
            if key.startswith("DT43_"):
                clean_key = key[5:].lower()
                instance._settings[clean_key] = value
        return instance

    def serialize(self) -> Dict[str, Any]:
        return dict(self._settings)

config = AppConfig.load_environment()
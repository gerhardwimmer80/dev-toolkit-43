from typing import Dict, Any, Union, Final
import os

ConfigurationType = Dict[str, Union[str, int, bool]]

class AppConfig:
    """Dynamic configuration loader with fallback mechanisms."""

    _defaults: Final[ConfigurationType] = {
        "port": 8080,
        "debug": False,
        "environment": "production"
    }

    def __init__(self, prefix: str = "DEV_") -> None:
        """Initialize config object with optional environment variable prefix."""
        self._prefix: str = prefix
        self._cache: ConfigurationType = self._defaults.copy()
        self._load_from_env()

    def _load_from_env(self) -> None:
        """Scan process environment for matching configuration overrides."""
        for key in self._defaults:
            env_val = os.getenv(f"{self._prefix}{key.upper()}")
            if env_val:
                self._cache[key] = type(self._defaults[key])(env_val)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve value from cached configuration map."""
        return self._cache.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """Dict-like access for configuration items."""
        return self._cache[key]

    @property
    def settings(self) -> ConfigurationType:
        """Read-only view of active configuration parameters."""
        return {**self._cache}

config = AppConfig()
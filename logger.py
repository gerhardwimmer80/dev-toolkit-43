import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys
from typing import Optional


class DynamicRotatingLogger:
    """Singleton logger factory managing self-rotating log files with standard output."""

    _loggers: dict = {}

    @classmethod
    def get_logger(
        cls,
        name: str = "dev_toolkit",
        log_dir: str = "logs",
        max_mb: int = 2,
        backup_count: int = 3,
        level: int = logging.DEBUG,
    ) -> logging.Logger:
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.propagate = False

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s (line %(lineno)d): %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(logging.INFO)
        logger.addHandler(stdout_handler)

        path = Path(log_dir)
        path.mkdir(parents=True, exist_ok=True)
        log_file = path / f"{name}.log"

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_mb * 1024 * 1024,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

        cls._loggers[name] = logger
        return logger


def setup_toolkit_logger(
    name: str = "main", log_dir: Optional[str] = None
) -> logging.Logger:
    target_dir = log_dir or "logs"
    return DynamicRotatingLogger.get_logger(name=name, log_dir=target_dir)

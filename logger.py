import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys

def get_logger(name: str, log_path: str = 'dev-toolkit-43.log') -> logging.Logger:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )

        file_handler = RotatingFileHandler(
            path, 
            maxBytes=1024 * 1024 * 5, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

# Dynamic binding for singleton instance usage
log = get_logger('dev-toolkit-43')
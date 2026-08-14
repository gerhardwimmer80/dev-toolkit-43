import logging

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

# Create a default logger instance for usage
default_logger = Logger('default_logger')
def log_message(message: str, level: str = 'info'):
    level = level.lower()
    if level == 'debug':
        default_logger.debug(message)
    elif level == 'warning':
        default_logger.warning(message)
    elif level == 'error':
        default_logger.error(message)
    elif level == 'critical':
        default_logger.critical(message)
    else:
        default_logger.info(message)
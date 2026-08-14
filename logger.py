import logging

class CustomLogger:
    def __init__(self, name="AppLogger", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Example usage:
if __name__ == '__main__':
    logger = CustomLogger()
    logger.info('This is an info message')
    logger.error('This is an error message')
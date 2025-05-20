import logging

class LoggerUtil:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.DEBUG)
            
            # Create a file handler
            file_handler = logging.FileHandler('FastApiServices.log')
            file_handler.setLevel(logging.DEBUG)
            
            # Create a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)

            # Create a logging format
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add the handlers to the logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)


    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
    
    def log_debug(self, message):
        self.logger.debug(message)

# Usage:
# logger = LoggerUtil.getInstance()
# logger.log_info('This is an information message.')
# logger.log_warning('This is a warning message.')
# logger.log_error('This is an error message.')

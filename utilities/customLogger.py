import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        # Ensure the Logs directory exists
        log_directory = ".\\Logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Define the log file path
        log_file = os.path.join(log_directory, "automation.log")

        # Create a logger
        logger = logging.getLogger('automation_logger')
        logger.setLevel(logging.INFO)

        # Check if the logger already has handlers to avoid duplicate logs
        if not logger.handlers:
            # Create a file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.INFO)

            # Create a logging format
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)

            # Add the handlers to the logger
            logger.addHandler(file_handler)

        return logger



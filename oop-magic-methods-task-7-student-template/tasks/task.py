from contextlib import ContextDecorator
from datetime import datetime


class LogFile(ContextDecorator):
    def __init__(self, log_name: str):
        self.log_name = log_name
        with open(self.log_name, 'a') as self.log_file:
            pass

    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time = datetime.now() - self.start_time

        with open(self.log_name, 'r') as self.log_file:
            log = self.log_file.read()

        if exc_type is None:
            log += f'Start: {self.start_time} | Run: {self.time} | An error occurred: {exc_val}\n'
        else:
            log = f'Start: {self.start_time} | Run: {self.time} | An error occurred: {exc_val}\n' + log

        with open(self.log_name, 'w') as self.log_file:
            self.log_file.write(log)

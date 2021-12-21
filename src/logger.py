from configs import tests as conf
import logging


class Logger:
    def __init__(self, logfile_name: str):
        with open(f"{conf.logs}/{logfile_name}", 'w') as logger:
            self.logger = logger

    def report_warning(self, message: str):
        ...

    def report_error(self, message: str):
        ...

    def report_info(self, message: str):
        ...


from configs import tests as conf
import logging


class Logger:
    def __init__(self):#, logfile_name: str):
        fhand = open(f"{conf.logs}/anime.log", 'w')
        self.logger = logging.getLogger(f"{conf.logs}/anime.log")

    def report_warning(self, message: str):
        self.logger.warning(f"{message}")

    def report_error(self, message: str):
        self.logger.error(f"{message}")

    def report_info(self, message: str):
        self.logger.info(f"{message}")


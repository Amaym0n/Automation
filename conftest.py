# fixtures

import pytest
from os import mkdir
from os.path import exists
from configs import tests as conf
from src.logger import Logger


@pytest.fixture(scope='session', autouse=True)
def main_fixture(request):

    LOGGER = Logger()
    LOGGER.report_info("Logger was created")

    try:

        if not exists(conf.logs):
            mkdir(conf.logs)
        if not exists(conf.inputs):
            mkdir(conf.inputs)
        if not exists(conf.outputs):
            mkdir(conf.outputs)

    except Exception as exc:
        LOGGER.report_error(f"{exc}")
        raise


@pytest.fixture(scope='session', autouse=True)
def params_parser(request):
    ...
    #pytest.addoption("--logfile")

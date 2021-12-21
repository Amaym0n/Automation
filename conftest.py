# fixtures

import pytest
from os import mkdir
from os.path import exists
from configs import tests as conf
from src.logger import Logger


@pytest.fixture(scope='session', autouse=True)
def main_fixture():


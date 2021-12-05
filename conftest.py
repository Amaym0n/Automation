# fixtures

import pytest
from os import mkdir
from os.path import exists
from configs import tests as conf


@pytest.fixture(scope='session', autouse=True)
def main_fixture():
    print('\nTesting started')
    for path in [conf.logs, conf.outputs, conf.inputs]:
        if not exists(path):
            mkdir(path)

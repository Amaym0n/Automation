# fixtures

import pytest


@pytest.fixture(scope='session', autouse=True)
def main_fixture():
    print('\nTesting started')

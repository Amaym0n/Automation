import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(scope='session', autouse=True)
def params_parser(request: SubRequest):
    """CLI-params parser"""
    ...
    # pytest.addoption("--logfile")

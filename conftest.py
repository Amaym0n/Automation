import os
from pathlib import Path

import allure
from pytest import Config
from pytest import Parser

PROJECT_ROOT: str = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser: Parser) -> None:
    """ Expected options parser """
    parser.addoption(
        '--stand', action='store', default='stand1', help='stands: stand1/stand2'
    )


def pytest_configure(config: Config):
    """ Custom-marks """
    config.addinivalue_line('markers', 'api_test: API cases')
    config.addinivalue_line('markers', 'ui_test: UI cases')


pytest_plugins = [
    'fixtures.configs',
]


def create_path_to_file(file_name: str, custom_path: str = None) -> str:
    """ Dynamic creation of path to file """
    with allure.step(title=f'Create file path for file "{file_name}" '):
        path = custom_path if custom_path else PROJECT_ROOT
        for path in Path(path).rglob(pattern=file_name):
            return str(path)

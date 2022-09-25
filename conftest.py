import json
import os
from pathlib import Path
from typing import Any

import pytest
from _pytest.fixtures import SubRequest

PROJECT_ROOT: str = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser) -> None:
    """ Парсер ожидаемых аргументов """
    parser.addoption("--stand", action="store", default="stand1", help="stands: stand1/stand2")


def pytest_configure(config):
    """ Добавление custom-марки в проект """
    config.addinivalue_line("markers",
                            "test_data: Тесты добавляющие/заполняющие необходимые данные перед запуском основного АТ")
    config.addinivalue_line("markers",
                            "merge_test: Тесты покрывающие критический функционал. Используются для влития в мастер")
    config.addinivalue_line("markers", "api_test: Тесты покрывающие REST-запросы")
    config.addinivalue_line("markers", "ui_test: Тесты покрывающие UI")
    config.addinivalue_line("markers", "contract_test: Контрактные тесты")


@pytest.fixture(scope='session', autouse=True)
def conf(request: SubRequest) -> dict[str, Any]:
    """ Получение конфигов стенда """
    stand_name: str = request.config.getoption("--stand")
    with open(file=os.path.join(PROJECT_ROOT, 'configs', stand_name), mode='r') as stand_config:
        return json.loads(s=stand_config.read())


def create_path_to_file(file_name: str, custom_path: str = None) -> str:
    """ Динамическое создание пути к указанному файлу путем поиска его в переданном пути или в корне проекта """
    path = custom_path if custom_path else PROJECT_ROOT
    for path in Path(path).rglob(pattern=file_name):
        return str(path)

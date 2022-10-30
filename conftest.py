import json
import os
from pathlib import Path
from typing import Any, Union

import allure
import pytest
from _pytest.fixtures import SubRequest

from clients.RestClient import RestClient, Headers
from test_data.basic_enums import User
from test_data.project_urls import Urls

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
    config.addinivalue_line("markers", "smoke_test: Контрактные тесты")


@pytest.fixture(scope='session', autouse=True)
def conf(request: SubRequest) -> dict[str, Any]:
    """ Получение конфигов стенда """
    with allure.step('Получение конфигов стенда'):
        stand_name: str = request.config.getoption("--stand")
        with open(file=os.path.join(PROJECT_ROOT, 'configs', stand_name), mode='r') as stand_config:
            return json.loads(s=stand_config.read())


@pytest.fixture(scope='function', autouse=True, name='test_params')
def get_test_params_from_parametrize(request: SubRequest) -> Union[dict[str, Any], dict]:
    with allure.step('Получение параметров теста из pytest.mark.parametrize'):
        try:
            return request.node.callspec.params
        except AttributeError:
            return {}


@pytest.fixture(scope='function')
def get_access_token(conf: dict[str, Any], test_params: Union[dict[str, Any], dict]) -> str:
    """ Фикстура для получения Access-токена """
    user = User.SUPERVISOR if not test_params.get('user', False) else test_params.get('user')
    with allure.step(f'Получение Access-токена для {user}'):
        data = {'username': user.get_username(), 'password': user.get_password()}
        response = RestClient(conf=conf).post(path=Urls.login_for_access_token.url,
                                              data=data, headers=Headers.DATA_TYPE.value)
    return response.json()['access_token']


@pytest.fixture(scope='function')
def get_refresh_token(conf: dict[str, Any], test_params: Union[dict[str, Any], dict]) -> str:
    """ Фикстура для получения Refresh-токена """
    user = User.SUPERVISOR if not test_params.get('user', False) else test_params.get('user')
    with allure.step(f'Получение Refresh-токена для {user}'):
        data = {'username': user.get_username(), 'password': user.get_password()}
        response = RestClient(conf=conf).post(path=Urls.login_for_access_token.url,
                                              data=data, headers=Headers.DATA_TYPE.value)
    return response.json()['refresh_token']


@pytest.fixture(scope='function')
def create_multiple_headers(test_params: Union[dict[str, Any], dict], get_access_token: str) -> Headers:
    """ Создание мульти-хэдера """
    with allure.step('Создание мульти-хэдера'):
        headers = Headers.JSON_TYPE.jwt_headers(jwt_token=get_access_token) \
            if not test_params.get('headers', False) \
            else test_params.get('headers').jwt_headers(jwt_token=get_access_token)
        return headers


def create_path_to_file(file_name: str, custom_path: str = None) -> str:
    """ Динамическое создание пути к указанному файлу путем поиска его в переданном пути или в корне проекта """
    with allure.step(f'Создание пути до файла {file_name}'):
        path = custom_path if custom_path else PROJECT_ROOT
        for path in Path(path).rglob(pattern=file_name):
            return str(path)

from __future__ import annotations

from enum import Enum
from http import HTTPStatus
from typing import Any, Optional, Union

import allure
import requests
from requests import Response


class Headers(Enum):
    """ Headers проекта для передачи в requests """

    NONE_TYPE: Headers = None
    JSON_TYPE: Headers = {'Content-Type': 'application/json'}
    DATA_TYPE: Headers = {"Content-Type": "application/x-www-form-urlencoded"}
    MULTIPART_TYPE: Headers = {'Content-Type': 'multipart/form-data'}
    JWT_TYPE: Headers = {}

    def jwt_headers(self, jwt_token: str) -> Headers:
        """ Генерация мульти-хэдера """
        self.value['Authorization'] = self.value.get('Authorization', jwt_token)
        return self


class RestClient:
    """ Класс для взаимодействия с REST """

    def __init__(self, conf: dict[str, Any], cookies: Optional[dict[str, str]] = None) -> None:
        self.conf: dict[str, Any] = conf
        self.cookies: dict[str, str] = cookies
        self.basic_path: str = f'{conf["protocol"]}{conf["url"]}'

    def get(self, path: str, params: Optional[dict] = None, headers: Optional[Headers] = None,
            status_code: int = HTTPStatus.OK) -> Response:
        """ Формирование и отправка GET-запроса """
        with allure.step(title=f'GET-запрос по url -> {self.basic_path}{path}'):
            response = requests.get(url=f'{self.basic_path}{path}', params=params,
                                    headers=headers, cookies=self.cookies, timeout=300,
                                    verify=False)
            self._check_status_code(response_status=response, expected_status_code=status_code)
        return response

    def post(self, path: str, headers: Headers, params: Optional[dict] = None, data: Any = None,
             json: Optional[dict] = None, files: Union[dict, list, None] = None,
             status_code: int = HTTPStatus.OK) -> Response:
        """ Формирование и отправка POST-запроса """
        with allure.step(title=f'POST-запрос по url -> {self.basic_path}{path}'):
            response = requests.post(url=f'{self.basic_path}{path}', params=params, data=data, json=json,
                                     headers=headers, cookies=self.cookies, files=files, timeout=300,
                                     verify=False)
            self._check_status_code(response_status=response, expected_status_code=status_code)
        return response

    def delete(self, path: str, headers: Headers, params: Optional[dict] = None,
               status_code: int = HTTPStatus.OK) -> Response:
        """ Формирование и отправка DELETE-запроса """
        with allure.step(title=f'DELETE-запрос по url -> {self.basic_path}{path}'):
            response = requests.delete(url=f'{self.basic_path}{path}',
                                       headers=headers, params=params, cookies=self.cookies, timeout=300,
                                       verify=False)
            self._check_status_code(response_status=response, expected_status_code=status_code)
        return response

    @staticmethod
    def _check_status_code(response_status: Response, expected_status_code: int = HTTPStatus.OK) -> None:
        with allure.step(title='Проверка статуса из полученного response'):
            assert response_status.status_code == expected_status_code, \
                f'Полученный REST-запросом статус код {response_status.status_code} ' \
                f'не соответствует ожидаемому {expected_status_code}'

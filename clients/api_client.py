from __future__ import annotations

from http import HTTPStatus
from typing import Any
from typing import Callable

import allure
import requests
from requests import Response

from basic_helper.object_description import StandConfig
from clients.auth.jwt_auth import JWTAuth


def timeout_logging(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to add requests when request fails due to timeout"""

    def logging(*args: object, **kwargs: dict[str, Any]) -> Response:
        try:
            return func(*args, **kwargs)
        except requests.exceptions.Timeout as e:
            with allure.step(f"[{e.request.method}] --> {e.request.url}"):
                req_text = f"""[{e.request.method}] --> {e.request.url} \n'
                           headers: {e.request.headers} \n body: {e.request.body if e.request.body else ""}"""
                allure.attach(req_text, "request", allure.attachment_type.TEXT)
                raise requests.exceptions.Timeout(e)

    return logging


def allure_listener(response: Response, *args: Any, **kwargs: Any) -> None:
    """ Function for logging requests and responses for ApiClient """

    def formatter(resp: Response) -> tuple[str, str]:
        """ Formatting information for logging """
        req_data = (
            f'[{resp.request.method}] --> {resp.url} \n' f' headers: {resp.headers}'
        )
        if resp.request.method == 'POST':
            req_data += f'\n body: {resp.request.body}'
        req_message = req_data
        resp_message = (
            f'status_code: {resp.status_code} \n {req_data} \n Content: \n {resp.text}'
        )
        return req_message, resp_message

    with allure.step(f"[{response.request.method}] --> {response.url}"):
        req_text, resp_text = formatter(response)
        allure.attach(req_text, 'request', allure.attachment_type.TEXT)
        allure.attach(resp_text, 'response', allure.attachment_type.TEXT)


class ApiClient:
    def __init__(self, config: StandConfig, auth: JWTAuth) -> None:
        self.base_url = f'{config.protocol}{config.url}'
        self.auth = auth

    @timeout_logging
    def request(
            self,
            method: str,
            path: str,
            headers: dict,
            params: dict,
            data: dict | None = None,
            json: dict | None = None,
            files: dict | list | None = None,
            allow_redirects: bool = True,
            verify: bool = False,
            status_code: int = HTTPStatus.OK,
    ):
        """ Send HTTP-request """
        response = requests.request(
            method=method,
            url=f'{self.base_url}{path}',
            headers=headers, params=params,
            data=data, json=json,
            files=files,
            allow_redirects=allow_redirects,
            verify=verify
        )
        self.check_status_code(response=response, status_code=status_code)
        return response

    @staticmethod
    def check_status_code(response: Response, status_code: int) -> None:
        with allure.step('Checking the status of the request code'):
            assert response.status_code == status_code, \
                f"""Wrong status code, expected: {status_code}, received: {response.status_code}, 
                message: {response.text}"""

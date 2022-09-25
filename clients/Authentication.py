from __future__ import annotations

import json
from typing import Any

from requests import Response

from test_data.basic_enums import User
from clients.RestClient import RestClient, Headers
from test_data.project_urls import Urls


class Authentication:
    """ Авторизация пользователя, получение cookies"""

    def __init__(self, conf: dict[str, Any], user: User = User.USER) -> None:
        self.conf = conf
        self.user = user
        self.response = None

    def get_authorization(self) -> Authentication:
        """ Авторизация под пользователем """
        data = {'username': self.user.get_username(), 'password': self.user.get_password()}
        self.response = RestClient(conf=self.conf).post(path=Urls.login_for_auth_login_post.url,
                                                        data=data, headers=Headers.DATA_TYPE)
        return self

    def get_cookies(self) -> Response:
        """ Получение кукис """
        return self.response.cookies

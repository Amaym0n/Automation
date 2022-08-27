from http import HTTPStatus
from typing import Any

import requests

from clients.metaclasses import Singleton


class ApiClient(metaclass=Singleton):
    """Class to work with REST"""

    def __init__(self, conf: dict[str, Any], cookies: dict[str, str]):
        self.request = requests.Session()

    def get(self, path: str, params: dict[str, Any], headers, statuscode: HTTPStatus.OK):
        """GET request"""
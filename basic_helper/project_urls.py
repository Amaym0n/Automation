from __future__ import annotations

from enum import Enum
from enum import unique


class UrlsEnum(Enum):

    def __init__(self, url: str, description: str) -> None:
        self.url: str = url
        self.description: str = description

    def format_url(self, **kwargs) -> str:
        """ Format values in url """
        return self.url.format(**kwargs)


@unique
class Urls(UrlsEnum):
    """ Enum with project urls """

    login_for_auth: Urls = ('/api/auth/login', 'Login For Auth')

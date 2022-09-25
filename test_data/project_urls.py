from __future__ import annotations

from enum import unique, Enum


class UrlsEnum(Enum):
    """ Enum для взаимодействия с Urls """

    def __init__(self, url: str, description: str) -> None:
        self.url: str = url
        self.description: str = description

    def format_url(self, **kwargs) -> str:
        """ Заполнение вызываемого url'а переданными значениями используя метод .format """
        return self.url.format(**kwargs)


@unique
class Urls(UrlsEnum):
    """ Enum с url'ами проекта """

    # swagger
    swagger: Urls = ('/docs#', 'Swagger')

    login_for_auth: Urls = ('/api/auth/login', 'Login For Auth')

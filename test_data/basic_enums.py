from __future__ import annotations

from enum import Enum
from typing import Union


class FullEnum(Enum):
    """ Enum для получения значений ident, title из переменных """

    def __init__(self, ident: Union[str, int], title: str) -> None:
        self.ident = ident
        self.title = title


class User(Enum):
    """ Пользователи для взаимодействия с сервисом """

    SUPERVISOR: User = ('supervisor@example.com', 'supervisor')
    WENDI_USER: User = ('test@uktlab.ru', 'QLeBUmOxvE')

    def get_username(self) -> str:
        return self.value[0]

    def get_password(self) -> str:
        return self.value[1]

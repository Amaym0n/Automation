from __future__ import annotations

from enum import Enum


class BasicEnum(Enum):
    """ Базовый Enum с общими методами для работы """

    def __init__(self, title: str) -> None:
        self.title: str = title


class User(Enum):
    """ Пользователи для взаимодействия с сервисом """

    SUPERVISOR: User = ('username', 'password]')
    INVALID_USER: User = ('auto', 'mation')

    def get_username(self) -> str:
        return self.value[0]

    def get_password(self) -> str:
        return self.value[1]

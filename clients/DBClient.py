from __future__ import annotations

from typing import Any, Optional

import allure
import psycopg2
from psycopg2._psycopg import cursor, connection


class DBClient:
    """ Клиент для работы с БД - postgresql """

    def __init__(self, connection_string: dict[str, str]) -> None:
        self.connection_string = connection_string
        self.connection: Optional[connection] = None
        self.cursor: Optional[cursor] = None

    def get_first_value(self, query: str) -> Any:
        """ Получить первое значение по переданному SQL-запросу """
        with allure.step('Получение первого значения из переданного запроса'):
            self.cursor.execute(query=query)
            if not (result := self.cursor.fetchone()):
                return None
            return result[0]

    def get_list(self, query: str) -> list[Any]:
        """ Получение списка по переданному SQL-запросу """
        with allure.step('Получение списка из переданного запроса'):
            self.cursor.execute(query=query)
            return list(self.cursor.fetchone())

    def get_first_row(self, query: str) -> tuple[Any]:
        """ Получение первой строки по переданному SQL-запросу """
        with allure.step('Получение первой строки для переданного запроса'):
            self.cursor.execute(query=query)
            return self.cursor.fetchone()

    def __enter__(self) -> DBClient:
        self.connection = psycopg2.connect(database=self.connection_string['db'],
                                           user=self.connection_string['username'],
                                           password=self.connection_string['password'],
                                           host=self.connection_string['host'],
                                           port=self.connection_string['port'])
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.cursor.close()
        self.connection.close()

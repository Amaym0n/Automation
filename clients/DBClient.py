from __future__ import annotations

import json
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

    def get_first_value(self, query: str) -> tuple[Any]:
        """ Получить первое значение по переданному SQL-запросу """
        with allure.step('Получение первого значения из переданного запроса'):
            self.cursor.query(query)
            return self.cursor.fetchall()[0]

    def get_list(self, query: str) -> list[Any]:
        """ Получение списка по переданному SQL-запросу """
        with allure.step('Получение списка из переданного запроса'):
            self.cursor.query(query)
            return list(self.cursor.fetchone())

    def get_json(self, query: str) -> dict[str, Any]:
        """ Получение JSON по переданному SQL-запросу """
        # TODO: Необходимо исправить реализацию. Так как не открывается BLOB
        with allure.step('Получение JSON из БД таблицы'):
            self.cursor.query(query=query)
            return json.loads(self.cursor.fetchone()[0])

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

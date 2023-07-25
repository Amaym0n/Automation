from __future__ import annotations

import functools
from typing import Callable, Any

import allure
import psycopg2
from psycopg2.extensions import connection
from psycopg2.extensions import cursor


def allure_listener(func: Callable[..., Any]) -> Callable[..., Any]:
    """ Decorator that attaches the SQL query as an allure attachment """

    @functools.wraps(wrapped=func)
    def wrapper(self: DBClient, query: str, *args: Any, **kwargs: Any) -> Any:
        """ Wrapper function that attaches the SQL query and vars as an allure attachment """
        result = func(self, query, *args, **kwargs)
        with allure.step(title='SQL query and query result --->'):
            allure.attach(query, name='SQL Query', attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(result), name='SQL Result', attachment_type=allure.attachment_type.TEXT)
        return result

    return wrapper


class DBClient:
    """ Object that helps to easily work with db """

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string
        self.connection: connection | None = None
        self.cursor: cursor | None = None

    @allure_listener
    def get_first_row(self, query: str) -> ...:
        """ Get first row from query result """
        self.cursor.execute(query=query)
        return self.cursor.fetchone()

    @allure_listener
    def select_all(self, query: str) -> list[tuple[...]]:
        self.cursor.execute(query=query)
        return self.cursor.fetchall()

    def __enter__(self) -> DBClient:
        """ Connect to database """
        self.connection = psycopg2.connect(dsn=self.connection_string)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ Close database connection """
        self.cursor.close()
        self.connection.close()
        return

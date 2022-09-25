import allure
import pytest

from clients.DBClient import DBClient
from conftest import create_path_to_file


@pytest.mark.test_data
@pytest.mark.parametrize('file_name', ['sql_query.sql'])
def test_insert_data_to_db(conf, file_name):
    file_root = create_path_to_file(file_name=file_name)
    with open(file=file_root, mode='rb') as sql_queries:
        queries = [query.strip('/r/n') for query in sql_queries.read().decode().split(';')]
    with allure.step('Создание необходимых записей в БД'):
        with DBClient(connection_string=conf['connection_string']) as db:
            for query in queries:
                db.cursor.execute(query=query)

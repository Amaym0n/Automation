import json
from http import HTTPStatus

import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(scope='function')
def get_base_schema(request: SubRequest, status_code: HTTPStatus) -> dict[str, str]:
    path = request.fspath.dirname
    with open(file=f'{path}//base.schema.json', mode='rb') as base_schema:
        base_schema = json.load(fp=base_schema).get(str(status_code))
    return base_schema


@pytest.fixture(scope='function')
def get_definitions_schema(request: SubRequest, status_code: HTTPStatus) -> dict[str, str]:
    path = request.fspath.dirname
    with open(file=f'{path}//definitions.schema.json', mode='rb') as definitions_schema:
        definitions_schema = json.load(fp=definitions_schema).get(str(status_code))
    return definitions_schema

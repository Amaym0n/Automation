from http import HTTPStatus

import pytest

from clients.RestClient import RestClient, Headers
from schema_construct import SchemaConstruct
from test_data.basic_enums import User
from test_data.project_urls import Urls


@pytest.mark.api_test
@pytest.mark.contract_test
@pytest.mark.parametrize('status_code, user', [(HTTPStatus.OK, User.USER),
                                               (HTTPStatus.UNAUTHORIZED, User.INVALID_USER)])
def test_login_for_access_token(conf, status_code, user, get_base_schema):
    data = {'username': user.get_username(), 'password': user.get_password()}
    response = RestClient(conf=conf).post(path=Urls.login_for_auth.url,
                                          data=data, headers=Headers.DATA_TYPE, status_code=status_code)
    SchemaConstruct(base_schema=get_base_schema, definitions_schema=None).validation(response=response.content)

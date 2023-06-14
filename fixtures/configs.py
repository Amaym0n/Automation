import json
import os
from collections import namedtuple

import allure
import pytest
from _pytest.fixtures import SubRequest

from basic_helper.object_description import StandConfig
from conftest import PROJECT_ROOT


@pytest.fixture(scope='session', autouse=True)
def load_env():
    """ Fixture that helps to work with tests locally """
    if not os.getenv(key='PG_CONNECTION_STRING'):
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, '.env'))
    return


@pytest.fixture(scope="session", autouse=True)
def conf(load_env: None, request: SubRequest) -> StandConfig:
    """ Fixture that helps to get stand configs """
    with allure.step(title='Get stand configs from env and config file'):
        stand_name: str = request.config.getoption('--stand')
        with open(
                file=os.path.join(PROJECT_ROOT, 'configs', stand_name)
        ) as stand_config:
            stand_config = json.loads(s=stand_config.read())
        stand_config['db_connection_string'] = os.getenv(key='PG_CONNECTION_STRING')
        return namedtuple('config', stand_config.keys())(**stand_config)


@pytest.fixture(scope='function', autouse=True, name='test_params')
def get_test_params_from_parametrize(
        request: SubRequest,
) -> dict:
    """ Fixture that helps to get test params for each parametrized cases """
    with allure.step(title='Get test params from pytest.mark.parametrize'):
        try:
            return request.node.callspec.params
        except AttributeError:
            return {}

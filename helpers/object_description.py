from typing import NamedTuple

from pydantic import BaseSettings


class StandConfig(NamedTuple):
    """ Stand configs description """
    protocol: str
    url: str
    db_connection_string: str


class ENVConfigs(BaseSettings):
    """ Your ENV variables here """
    username: str
    password: str

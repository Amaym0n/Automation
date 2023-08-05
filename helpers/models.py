from typing import NamedTuple

from pydantic import BaseSettings


class StandConfig(NamedTuple):
    """ Stand configs description """
    # Add variables which you want to get from config
    protocol: str
    url: str
    db_connection_string: str


class ENVConfigs(BaseSettings):
    """ Your ENV variables here """
    # Add all environment variables you need
    username: str
    password: str

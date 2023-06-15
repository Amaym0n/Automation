from typing import NamedTuple


class StandConfig(NamedTuple):
    """ Stand configs description """
    protocol: str
    url: str
    db_connection_string: str

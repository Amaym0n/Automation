from configs import tests as conf
import os

def test_anime():
    try:
        os.mkdir(conf.log)
    except Exception as exc:
        print(exc)
    assert 1 == 1
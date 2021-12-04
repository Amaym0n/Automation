from configs import tests as conf
import os

def test_anime():
    try:
        os.system(f'cmd /c "mkdir {conf.log}"')
    except Exception as exc:
        print(exc)
    assert 1 == 1
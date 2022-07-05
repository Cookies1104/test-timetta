import pytest

from auth_token import AuthToken


@pytest.fixture(scope='session')
def access_token():
    """Возвращает access_token """
    yield AuthToken().access_token

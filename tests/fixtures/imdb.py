import pytest

from asynctmdb import imdb


@pytest.fixture(scope='function')
def imdb_id() -> str:
    return imdb.title_id.int_to_str(1)


@pytest.fixture(scope='function')
def non_existent_imdb_id() -> str:
    return imdb.title_id.int_to_str(0)


@pytest.fixture(scope='function')
def invalid_imdb_id() -> str:
    return ''

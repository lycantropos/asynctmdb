import pytest

from asynctmdb import imdb


@pytest.fixture(scope='function')
def imdb_id() -> str:
    return imdb.title_id.int_to_str(1)

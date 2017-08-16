import os

import pytest

from asynctmdb.utils import urljoin


@pytest.fixture(scope='session')
def api_key() -> str:
    return os.environ['API.Key']


@pytest.fixture(scope='session')
def api_base_url() -> str:
    return urljoin(os.environ['API.BaseURL'],
                   os.environ['API.Version'])

import os
import pkgutil
import sys
from asyncio import (get_event_loop,
                     ensure_future)
from contextlib import closing
from typing import List

import pytest
from _pytest.config import Parser
from _pytest.python import Metafunc
from aiohttp import ClientSession

from asynctmdb import requests

base_dir = os.path.dirname(__file__)
sys.path.append(base_dir)


def explore_pytest_plugins(base_dir: str,
                           fixtures_pkg_name: str) -> List[str]:
    fixtures_pkg_path = os.path.join(base_dir,
                                     fixtures_pkg_name)
    return [f'{fixtures_pkg_name}.{name}'
            for _, name, _ in pkgutil.iter_modules([fixtures_pkg_path])]


pytest_plugins = explore_pytest_plugins(base_dir=base_dir,
                                        fixtures_pkg_name='fixtures')


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--repeat',
                     action='store',
                     help='Number of times to repeat each test.')


def pytest_generate_tests(metafunc: Metafunc) -> None:
    if metafunc.config.option.repeat is None:
        return
    count = int(metafunc.config.option.repeat)
    # We're going to duplicate these tests by parametrisation,
    # which requires that each test has a fixture to accept the parameter.
    # We can add a new fixture like so:
    metafunc.fixturenames.append('tmp_ct')
    # Now we parametrize. This is what happens when we do e.g.,
    # @pytest.mark.parametrize('tmp_ct', range(count))
    # def test_foo(): pass
    metafunc.parametrize('tmp_ct', range(count))


@pytest.fixture(scope='session',
                autouse=True)
def preparation(api_base_url: str,
                api_key: str) -> None:
    event_loop = get_event_loop()
    with ClientSession(loop=event_loop) as session:
        future = ensure_future(requests.get(method_url=api_base_url,
                                            session=session,
                                            api_key=api_key))
        event_loop.run_until_complete(future)

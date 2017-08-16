from asyncio import AbstractEventLoop, ensure_future

import pytest
from aiohttp import ClientSession

from asynctmdb.methods.authentication import create_request_token


@pytest.fixture(scope='function')
def request_token(api_base_url: str,
                  api_key: str,
                  session: ClientSession,
                  event_loop: AbstractEventLoop) -> str:
    future = ensure_future(create_request_token(api_base_url=api_base_url,
                                                api_key=api_key,
                                                session=session))
    response = event_loop.run_until_complete(future)
    return response['request_token']

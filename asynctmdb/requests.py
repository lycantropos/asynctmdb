from functools import partial
from typing import (Any,
                    Callable,
                    Dict)

from aiohttp import ClientSession

from .types import AsyncContextManager


async def send(*,
               method: Callable[[ClientSession, str, Any],
                                AsyncContextManager],
               method_url: str,
               session: ClientSession,
               **params: Dict[str, str]
               ) -> Dict[str, Any]:
    async with method(session,
                      method_url,
                      params=params) as response:
        response_json = await response.json()
        return response_json


get = partial(send,
              method=ClientSession.get)
post = partial(send,
               method=ClientSession.post)

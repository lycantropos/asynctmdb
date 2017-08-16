from typing import (Union,
                    Dict,
                    List)

from aiohttp import ClientSession

from asynctmdb import requests
from asynctmdb.utils import urljoin

GenresType = List[Dict[str, Union[int, str]]]


async def movie(*,
                api_base_url: str,
                api_key: str,
                language: str = 'en-US',
                session: ClientSession) -> GenresType:
    method_url = urljoin(api_base_url, 'genre/movie/list')
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key,
                                  language=language)
    return response['genres']


async def tv(*,
             api_base_url: str,
             api_key: str,
             language: str = 'en-US',
             session: ClientSession) -> GenresType:
    method_url = urljoin(api_base_url, 'genre/tv/list')
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key,
                                  language=language)
    return response['genres']

from functools import partial

from aiohttp import ClientSession

from asynctmdb import requests
from asynctmdb.utils import urljoin

external_sources = {'imdb_id',
                    'freebase_mid', 'freebase_id',
                    'tvdb_id', 'tvrage_id'}


async def find_by_id(external_id: str,
                     *,
                     api_base_url: str,
                     api_key: str,
                     language: str = 'en-US',
                     external_source: str,
                     session: ClientSession) -> dict:
    method_url = urljoin(api_base_url, 'find', external_id)
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key,
                                  language=language,
                                  external_source=external_source)
    return response


find_by = {external_source: partial(find_by_id,
                                    external_source=external_source)
           for external_source in external_sources}

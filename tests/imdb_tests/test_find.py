import pytest
from aiohttp import ClientSession

from asynctmdb import imdb


@pytest.mark.asyncio
async def test_find_by_imdb_id(api_base_url: str,
                               api_key: str,
                               imdb_id: str,
                               session: ClientSession) -> None:
    response = await imdb.find.movie(imdb_id,
                                     api_base_url=api_base_url,
                                     api_key=api_key,
                                     session=session)

    assert isinstance(response, dict)
    assert 'title' in response
    assert response['title'] == 'Carmencita'

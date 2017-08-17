import pytest
from aiohttp import ClientSession

from asynctmdb import imdb


@pytest.mark.asyncio
async def test_find_by_imdb_id(api_base_url: str,
                               api_key: str,
                               imdb_id: str,
                               invalid_imdb_id: str,
                               non_existent_imdb_id: str,
                               session: ClientSession) -> None:
    response = await imdb.find.movie(imdb_id,
                                     api_base_url=api_base_url,
                                     api_key=api_key,
                                     session=session)

    with pytest.raises(ValueError):
        await imdb.find.movie(invalid_imdb_id,
                              api_base_url=api_base_url,
                              api_key=api_key,
                              session=session)
    with pytest.raises(ValueError):
        await imdb.find.movie(non_existent_imdb_id,
                              api_base_url=api_base_url,
                              api_key=api_key,
                              session=session)

    assert isinstance(response, dict)
    assert 'title' in response
    assert response['title'] == 'Carmencita'

import operator

import pytest
from aiohttp import ClientSession

from asynctmdb.methods import genres


@pytest.mark.asyncio
async def test_movie_genres(api_base_url: str,
                            api_key: str,
                            session: ClientSession) -> None:
    movie_genres = await genres.movie(api_base_url=api_base_url,
                                      api_key=api_key,
                                      session=session)

    movie_genres_count = len(movie_genres)
    movie_genres_ids = list(map(operator.itemgetter('id'),
                                movie_genres))
    movie_genres_names = list(map(operator.itemgetter('name'),
                                  movie_genres))

    assert isinstance(movie_genres, list)
    assert all(isinstance(genre_id, int) and genre_id > 0
               for genre_id in movie_genres_ids)
    assert all(isinstance(genre_name, str) and genre_name
               for genre_name in movie_genres_names)

    assert len(set(movie_genres_ids)) == movie_genres_count
    assert len(set(movie_genres_names)) == movie_genres_count


@pytest.mark.asyncio
async def test_tv_genres(api_base_url: str,
                         api_key: str,
                         session: ClientSession) -> None:
    tv_genres = await genres.tv(api_base_url=api_base_url,
                                api_key=api_key,
                                session=session)

    tv_genres_count = len(tv_genres)
    tv_genres_ids = list(map(operator.itemgetter('id'),
                             tv_genres))
    tv_genres_names = list(map(operator.itemgetter('name'),
                               tv_genres))

    assert isinstance(tv_genres, list)
    assert all(isinstance(genre_id, int) and genre_id > 0
               for genre_id in tv_genres_ids)
    assert all(isinstance(genre_name, str) and genre_name
               for genre_name in tv_genres_names)

    assert len(set(tv_genres_ids)) == tv_genres_count
    assert len(set(tv_genres_names)) == tv_genres_count

from aiohttp import ClientSession

from asynctmdb.methods import find


async def movie(imdb_id: str,
                *,
                api_base_url: str,
                api_key: str,
                language: str = 'en-US',
                session: ClientSession) -> dict:
    response = await find.by['imdb_id'](imdb_id,
                                        api_base_url=api_base_url,
                                        api_key=api_key,
                                        language=language,
                                        session=session)
    records = response['movie_results']
    try:
        record, = records
    except ValueError as err:
        if records:
            err_msg = (f'Movie imdb id "{imdb_id}" is ambiguous: '
                       f'found {len(records)} records.')
        else:
            err_msg = ('No record found for movie with '
                       f'imdb id "{imdb_id}".')
        raise ValueError(err_msg) from err
    else:
        return record

from datetime import datetime
from typing import (Union,
                    Dict)

from aiohttp import ClientSession

from asynctmdb import requests
from asynctmdb.utils import urljoin

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S %Z'


async def create_request_token(*,
                               api_base_url: str,
                               api_key: str,
                               session: ClientSession,
                               date_time_format: str = DATE_TIME_FORMAT
                               ) -> Dict[str, Union[int, str, datetime]]:
    method_url = urljoin(api_base_url, 'authentication/token/new')
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key)
    try:
        expiration_date_time = response['expires_at']
    except KeyError:
        return response

    response['expires_at'] = datetime.strptime(expiration_date_time,
                                               date_time_format)
    return response


async def create_session(*,
                         api_base_url: str,
                         api_key: str,
                         request_token: str,
                         session: ClientSession
                         ) -> Dict[str, Union[int, str]]:
    method_url = urljoin(api_base_url, 'authentication/session/new')
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key,
                                  request_token=request_token)
    return response


async def create_guest_session(*,
                               api_base_url: str,
                               api_key: str,
                               session: ClientSession,
                               date_time_format: str = DATE_TIME_FORMAT
                               ) -> Dict[str, Union[int, str, datetime]]:
    method_url = urljoin(api_base_url, 'authentication/guest_session/new')
    response = await requests.get(method_url=method_url,
                                  session=session,
                                  api_key=api_key)
    try:
        expiration_date_time = response['expires_at']
    except KeyError:
        return response

    response['expires_at'] = datetime.strptime(expiration_date_time,
                                               date_time_format)
    return response

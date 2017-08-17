from datetime import datetime

import pytest
from aiohttp import ClientSession

from asynctmdb.methods.authentication import (create_request_token,
                                              create_session,
                                              create_guest_session)


@pytest.mark.asyncio
async def test_create_request_token(api_base_url: str,
                                    api_key: str,
                                    invalid_api_key: str,
                                    session: ClientSession) -> None:
    invalid_response = await create_request_token(api_base_url=api_base_url,
                                                  api_key=invalid_api_key,
                                                  session=session)
    valid_response = await create_request_token(api_base_url=api_base_url,
                                                api_key=api_key,
                                                session=session)

    status_code = invalid_response['status_code']
    succeed = valid_response['success']
    expiration_date_time = valid_response['expires_at']
    request_token = valid_response['request_token']

    assert status_code == 7
    assert succeed
    assert expiration_date_time >= datetime.utcnow()
    assert isinstance(request_token, str)


@pytest.mark.asyncio
async def test_create_session(api_base_url: str,
                              api_key: str,
                              request_token: str,
                              session: ClientSession) -> None:
    invalid_response = await create_session(api_base_url=api_base_url,
                                            api_key=api_key,
                                            request_token=request_token,
                                            session=session)

    status_code = invalid_response['status_code']

    assert status_code == 17


@pytest.mark.asyncio
async def test_create_guest_session(api_base_url: str,
                                    api_key: str,
                                    invalid_api_key: str,
                                    session: ClientSession) -> None:
    invalid_response = await create_guest_session(api_base_url=api_base_url,
                                                  api_key=invalid_api_key,
                                                  session=session)
    valid_response = await create_guest_session(api_base_url=api_base_url,
                                                api_key=api_key,
                                                session=session)

    status_code = invalid_response['status_code']
    succeed = valid_response['success']
    expiration_date_time = valid_response['expires_at']
    guest_session_id = valid_response['guest_session_id']

    assert status_code == 7
    assert succeed
    assert expiration_date_time >= datetime.utcnow()
    assert isinstance(guest_session_id, str)

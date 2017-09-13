from datetime import datetime

import pytest
from aiohttp import ClientSession

from asynctmdb.common import StatusCode
from asynctmdb.methods.authentication import (create_request_token,
                                              create_session,
                                              create_guest_session,
                                              validate_request_token)
from tests.utils import is_non_empty_string


@pytest.mark.asyncio
async def test_create_request_token(api_base_url: str,
                                    api_key: str,
                                    invalid_api_key: str,
                                    current_date_time: datetime,
                                    session: ClientSession) -> None:
    invalid_api_key_response = await create_request_token(
            api_base_url=api_base_url,
            api_key=invalid_api_key,
            session=session)
    valid_response = await create_request_token(
            api_base_url=api_base_url,
            api_key=api_key,
            session=session)

    invalid_api_key_status_code = invalid_api_key_response['status_code']
    succeed = valid_response['success']
    expiration_date_time = valid_response['expires_at']
    request_token = valid_response['request_token']

    assert invalid_api_key_status_code == StatusCode.INVALID_API_KEY
    assert isinstance(succeed, bool) and succeed
    assert expiration_date_time >= current_date_time
    assert is_non_empty_string(request_token)


@pytest.mark.asyncio
async def test_validate_request_token(api_base_url: str,
                                      api_key: str,
                                      invalid_api_key: str,
                                      user_name: str,
                                      user_password: str,
                                      request_token: str,
                                      session: ClientSession) -> None:
    valid_response = await validate_request_token(
            api_base_url=api_base_url,
            api_key=api_key,
            username=user_name,
            password=user_password,
            request_token=request_token,
            session=session)
    invalid_api_key_response = await validate_request_token(
            api_base_url=api_base_url,
            api_key=invalid_api_key,
            username=user_name,
            password=user_password,
            request_token=request_token,
            session=session)

    invalid_api_key_status_code = invalid_api_key_response['status_code']
    succeed = valid_response['success']
    valid_response_request_token = valid_response['request_token']

    assert invalid_api_key_status_code == StatusCode.INVALID_API_KEY
    assert isinstance(succeed, bool) and succeed
    assert is_non_empty_string(valid_response_request_token)
    assert valid_response_request_token == request_token


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

    assert status_code == StatusCode.SESSION_DENIED


@pytest.mark.asyncio
async def test_create_guest_session(api_base_url: str,
                                    api_key: str,
                                    invalid_api_key: str,
                                    session: ClientSession) -> None:
    invalid_api_key_response = await create_guest_session(
            api_base_url=api_base_url,
            api_key=invalid_api_key,
            session=session)
    valid_response = await create_guest_session(
            api_base_url=api_base_url,
            api_key=api_key,
            session=session)

    invalid_api_key_status_code = invalid_api_key_response['status_code']
    succeed = valid_response['success']
    expiration_date_time = valid_response['expires_at']
    guest_session_id = valid_response['guest_session_id']

    assert invalid_api_key_status_code == StatusCode.INVALID_API_KEY
    assert succeed
    assert expiration_date_time >= datetime.utcnow()
    assert isinstance(guest_session_id, str)

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environment_discovery_settings_response import EnvironmentDiscoverySettingsResponse
from ...models.environment_discovery_settings_update import EnvironmentDiscoverySettingsUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    env_id: UUID,
    *,
    body: EnvironmentDiscoverySettingsUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/environments/{env_id}/discovery-settings".format(
            env_id=quote(str(env_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EnvironmentDiscoverySettingsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    env_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EnvironmentDiscoverySettingsUpdate,
) -> Response[Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError]:
    """Update Environment Discovery Settings

     Update discovery settings for an environment

    Args:
        env_id (UUID):
        body (EnvironmentDiscoverySettingsUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        env_id=env_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    env_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EnvironmentDiscoverySettingsUpdate,
) -> Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError | None:
    """Update Environment Discovery Settings

     Update discovery settings for an environment

    Args:
        env_id (UUID):
        body (EnvironmentDiscoverySettingsUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError
    """

    return sync_detailed(
        env_id=env_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    env_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EnvironmentDiscoverySettingsUpdate,
) -> Response[Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError]:
    """Update Environment Discovery Settings

     Update discovery settings for an environment

    Args:
        env_id (UUID):
        body (EnvironmentDiscoverySettingsUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        env_id=env_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    env_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EnvironmentDiscoverySettingsUpdate,
) -> Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError | None:
    """Update Environment Discovery Settings

     Update discovery settings for an environment

    Args:
        env_id (UUID):
        body (EnvironmentDiscoverySettingsUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EnvironmentDiscoverySettingsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            env_id=env_id,
            client=client,
            body=body,
        )
    ).parsed

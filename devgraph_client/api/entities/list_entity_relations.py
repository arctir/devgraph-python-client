from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_relation_response import EntityRelationResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    namespace: str,
    managed_by: None | str | Unset = UNSET,
    source_type: None | str | Unset = UNSET,
    relation_type: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["namespace"] = namespace

    json_managed_by: None | str | Unset
    if isinstance(managed_by, Unset):
        json_managed_by = UNSET
    else:
        json_managed_by = managed_by
    params["managed_by"] = json_managed_by

    json_source_type: None | str | Unset
    if isinstance(source_type, Unset):
        json_source_type = UNSET
    else:
        json_source_type = source_type
    params["source_type"] = json_source_type

    json_relation_type: None | str | Unset
    if isinstance(relation_type, Unset):
        json_relation_type = UNSET
    else:
        json_relation_type = relation_type
    params["relation_type"] = json_relation_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/entities/relations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | list[EntityRelationResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EntityRelationResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | HTTPValidationError | list[EntityRelationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    namespace: str,
    managed_by: None | str | Unset = UNSET,
    source_type: None | str | Unset = UNSET,
    relation_type: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[EntityRelationResponse]]:
    """List relations with optional filtering

     Lists all relations in the namespace with optional filtering by labels. Requires
    'read:entityrelations' permission.

    Args:
        namespace (str):
        managed_by (None | str | Unset):
        source_type (None | str | Unset):
        relation_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[EntityRelationResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        managed_by=managed_by,
        source_type=source_type,
        relation_type=relation_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    namespace: str,
    managed_by: None | str | Unset = UNSET,
    source_type: None | str | Unset = UNSET,
    relation_type: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[EntityRelationResponse] | None:
    """List relations with optional filtering

     Lists all relations in the namespace with optional filtering by labels. Requires
    'read:entityrelations' permission.

    Args:
        namespace (str):
        managed_by (None | str | Unset):
        source_type (None | str | Unset):
        relation_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[EntityRelationResponse]
    """

    return sync_detailed(
        client=client,
        namespace=namespace,
        managed_by=managed_by,
        source_type=source_type,
        relation_type=relation_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    namespace: str,
    managed_by: None | str | Unset = UNSET,
    source_type: None | str | Unset = UNSET,
    relation_type: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError | list[EntityRelationResponse]]:
    """List relations with optional filtering

     Lists all relations in the namespace with optional filtering by labels. Requires
    'read:entityrelations' permission.

    Args:
        namespace (str):
        managed_by (None | str | Unset):
        source_type (None | str | Unset):
        relation_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError | list[EntityRelationResponse]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        managed_by=managed_by,
        source_type=source_type,
        relation_type=relation_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    namespace: str,
    managed_by: None | str | Unset = UNSET,
    source_type: None | str | Unset = UNSET,
    relation_type: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | list[EntityRelationResponse] | None:
    """List relations with optional filtering

     Lists all relations in the namespace with optional filtering by labels. Requires
    'read:entityrelations' permission.

    Args:
        namespace (str):
        managed_by (None | str | Unset):
        source_type (None | str | Unset):
        relation_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError | list[EntityRelationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            namespace=namespace,
            managed_by=managed_by,
            source_type=source_type,
            relation_type=relation_type,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_result_set_response import EntityResultSetResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    uids: list[str],
    namespace: str | Unset = "default",
    depth: int | Unset = 1,
    fields: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_uids = uids

    params["uids"] = json_uids

    params["namespace"] = namespace

    params["depth"] = depth

    json_fields: None | str | Unset
    if isinstance(fields, Unset):
        json_fields = UNSET
    else:
        json_fields = fields
    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/entities/uid/batch",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EntityResultSetResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EntityResultSetResponse.from_dict(response.json())

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
) -> Response[Any | EntityResultSetResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    uids: list[str],
    namespace: str | Unset = "default",
    depth: int | Unset = 1,
    fields: None | str | Unset = UNSET,
) -> Response[Any | EntityResultSetResponse | HTTPValidationError]:
    """Retrieve multiple entities by UIDs in a single request

     Fetches multiple entities by their unique identifiers (UIDs) in a single request. More efficient
    than multiple individual requests. Requires 'read:entities' permission.

    Args:
        uids (list[str]): List of entity UIDs to fetch
        namespace (str | Unset): Namespace to query Default: 'default'.
        depth (int | Unset): Number of relationship hops to traverse (0-5). 0 = no relationships.
            Default: 1.
        fields (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityResultSetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        uids=uids,
        namespace=namespace,
        depth=depth,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    uids: list[str],
    namespace: str | Unset = "default",
    depth: int | Unset = 1,
    fields: None | str | Unset = UNSET,
) -> Any | EntityResultSetResponse | HTTPValidationError | None:
    """Retrieve multiple entities by UIDs in a single request

     Fetches multiple entities by their unique identifiers (UIDs) in a single request. More efficient
    than multiple individual requests. Requires 'read:entities' permission.

    Args:
        uids (list[str]): List of entity UIDs to fetch
        namespace (str | Unset): Namespace to query Default: 'default'.
        depth (int | Unset): Number of relationship hops to traverse (0-5). 0 = no relationships.
            Default: 1.
        fields (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityResultSetResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        uids=uids,
        namespace=namespace,
        depth=depth,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    uids: list[str],
    namespace: str | Unset = "default",
    depth: int | Unset = 1,
    fields: None | str | Unset = UNSET,
) -> Response[Any | EntityResultSetResponse | HTTPValidationError]:
    """Retrieve multiple entities by UIDs in a single request

     Fetches multiple entities by their unique identifiers (UIDs) in a single request. More efficient
    than multiple individual requests. Requires 'read:entities' permission.

    Args:
        uids (list[str]): List of entity UIDs to fetch
        namespace (str | Unset): Namespace to query Default: 'default'.
        depth (int | Unset): Number of relationship hops to traverse (0-5). 0 = no relationships.
            Default: 1.
        fields (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityResultSetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        uids=uids,
        namespace=namespace,
        depth=depth,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    uids: list[str],
    namespace: str | Unset = "default",
    depth: int | Unset = 1,
    fields: None | str | Unset = UNSET,
) -> Any | EntityResultSetResponse | HTTPValidationError | None:
    """Retrieve multiple entities by UIDs in a single request

     Fetches multiple entities by their unique identifiers (UIDs) in a single request. More efficient
    than multiple individual requests. Requires 'read:entities' permission.

    Args:
        uids (list[str]): List of entity UIDs to fetch
        namespace (str | Unset): Namespace to query Default: 'default'.
        depth (int | Unset): Number of relationship hops to traverse (0-5). 0 = no relationships.
            Default: 1.
        fields (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityResultSetResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            uids=uids,
            namespace=namespace,
            depth=depth,
            fields=fields,
        )
    ).parsed

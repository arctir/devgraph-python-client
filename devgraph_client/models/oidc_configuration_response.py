from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OIDCConfigurationResponse")


@_attrs_define
class OIDCConfigurationResponse:
    """OIDC configuration for CLI authentication.

    This provides the necessary information for the CLI to authenticate
    users via the configured OIDC provider (e.g., Clerk).

        Attributes:
            issuer_url (str):
            client_id (str):
            authorization_endpoint (None | str | Unset):
            token_endpoint (None | str | Unset):
            jwks_uri (None | str | Unset):
    """

    issuer_url: str
    client_id: str
    authorization_endpoint: None | str | Unset = UNSET
    token_endpoint: None | str | Unset = UNSET
    jwks_uri: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issuer_url = self.issuer_url

        client_id = self.client_id

        authorization_endpoint: None | str | Unset
        if isinstance(self.authorization_endpoint, Unset):
            authorization_endpoint = UNSET
        else:
            authorization_endpoint = self.authorization_endpoint

        token_endpoint: None | str | Unset
        if isinstance(self.token_endpoint, Unset):
            token_endpoint = UNSET
        else:
            token_endpoint = self.token_endpoint

        jwks_uri: None | str | Unset
        if isinstance(self.jwks_uri, Unset):
            jwks_uri = UNSET
        else:
            jwks_uri = self.jwks_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuer_url": issuer_url,
                "client_id": client_id,
            }
        )
        if authorization_endpoint is not UNSET:
            field_dict["authorization_endpoint"] = authorization_endpoint
        if token_endpoint is not UNSET:
            field_dict["token_endpoint"] = token_endpoint
        if jwks_uri is not UNSET:
            field_dict["jwks_uri"] = jwks_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issuer_url = d.pop("issuer_url")

        client_id = d.pop("client_id")

        def _parse_authorization_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_endpoint = _parse_authorization_endpoint(d.pop("authorization_endpoint", UNSET))

        def _parse_token_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token_endpoint = _parse_token_endpoint(d.pop("token_endpoint", UNSET))

        def _parse_jwks_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jwks_uri = _parse_jwks_uri(d.pop("jwks_uri", UNSET))

        oidc_configuration_response = cls(
            issuer_url=issuer_url,
            client_id=client_id,
            authorization_endpoint=authorization_endpoint,
            token_endpoint=token_endpoint,
            jwks_uri=jwks_uri,
        )

        oidc_configuration_response.additional_properties = d
        return oidc_configuration_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

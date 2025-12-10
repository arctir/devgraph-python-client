from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenIntrospectionResponse")


@_attrs_define
class TokenIntrospectionResponse:
    """Response model for token introspection endpoint.

    Attributes:
        active (bool):
        scopes (list[str]):
        user (None | str | Unset):
        environment (None | str | Unset):
        token_type (str | Unset):  Default: 'Bearer'.
    """

    active: bool
    scopes: list[str]
    user: None | str | Unset = UNSET
    environment: None | str | Unset = UNSET
    token_type: str | Unset = "Bearer"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        scopes = self.scopes

        user: None | str | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        environment: None | str | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        token_type = self.token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "scopes": scopes,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if environment is not UNSET:
            field_dict["environment"] = environment
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user = _parse_user(d.pop("user", UNSET))

        def _parse_environment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        token_type = d.pop("token_type", UNSET)

        token_introspection_response = cls(
            active=active,
            scopes=scopes,
            user=user,
            environment=environment,
            token_type=token_type,
        )

        token_introspection_response.additional_properties = d
        return token_introspection_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.scopes_response_resource_groups import ScopesResponseResourceGroups
    from ..models.scopes_response_roles import ScopesResponseRoles
    from ..models.scopes_response_scopes import ScopesResponseScopes


T = TypeVar("T", bound="ScopesResponse")


@_attrs_define
class ScopesResponse:
    """Response model for the scopes metadata endpoint.

    Attributes:
        scopes (ScopesResponseScopes):
        resource_groups (ScopesResponseResourceGroups):
        roles (ScopesResponseRoles):
    """

    scopes: ScopesResponseScopes
    resource_groups: ScopesResponseResourceGroups
    roles: ScopesResponseRoles
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scopes = self.scopes.to_dict()

        resource_groups = self.resource_groups.to_dict()

        roles = self.roles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scopes": scopes,
                "resource_groups": resource_groups,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scopes_response_resource_groups import ScopesResponseResourceGroups
        from ..models.scopes_response_roles import ScopesResponseRoles
        from ..models.scopes_response_scopes import ScopesResponseScopes

        d = dict(src_dict)
        scopes = ScopesResponseScopes.from_dict(d.pop("scopes"))

        resource_groups = ScopesResponseResourceGroups.from_dict(d.pop("resource_groups"))

        roles = ScopesResponseRoles.from_dict(d.pop("roles"))

        scopes_response = cls(
            scopes=scopes,
            resource_groups=resource_groups,
            roles=roles,
        )

        scopes_response.additional_properties = d
        return scopes_response

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

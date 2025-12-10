from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScopeInfo")


@_attrs_define
class ScopeInfo:
    """Information about a single scope.

    Attributes:
        description (str):
        resource (str):
        action (str):
        minimum_role (str):
    """

    description: str
    resource: str
    action: str
    minimum_role: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        resource = self.resource

        action = self.action

        minimum_role = self.minimum_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "resource": resource,
                "action": action,
                "minimum_role": minimum_role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        resource = d.pop("resource")

        action = d.pop("action")

        minimum_role = d.pop("minimum_role")

        scope_info = cls(
            description=description,
            resource=resource,
            action=action,
            minimum_role=minimum_role,
        )

        scope_info.additional_properties = d
        return scope_info

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

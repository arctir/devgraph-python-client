from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentDiscoverySettingsResponse")


@_attrs_define
class EnvironmentDiscoverySettingsResponse:
    """
    Attributes:
        discovery_enabled (bool):
        discovery_image_id (None | Unset | UUID):
    """

    discovery_enabled: bool
    discovery_image_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discovery_enabled = self.discovery_enabled

        discovery_image_id: None | str | Unset
        if isinstance(self.discovery_image_id, Unset):
            discovery_image_id = UNSET
        elif isinstance(self.discovery_image_id, UUID):
            discovery_image_id = str(self.discovery_image_id)
        else:
            discovery_image_id = self.discovery_image_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discovery_enabled": discovery_enabled,
            }
        )
        if discovery_image_id is not UNSET:
            field_dict["discovery_image_id"] = discovery_image_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discovery_enabled = d.pop("discovery_enabled")

        def _parse_discovery_image_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discovery_image_id_type_0 = UUID(data)

                return discovery_image_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        discovery_image_id = _parse_discovery_image_id(d.pop("discovery_image_id", UNSET))

        environment_discovery_settings_response = cls(
            discovery_enabled=discovery_enabled,
            discovery_image_id=discovery_image_id,
        )

        environment_discovery_settings_response.additional_properties = d
        return environment_discovery_settings_response

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

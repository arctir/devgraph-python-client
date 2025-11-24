from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.discovery_image_response import DiscoveryImageResponse


T = TypeVar("T", bound="DiscoveryImageListResponse")


@_attrs_define
class DiscoveryImageListResponse:
    """Response for listing discovery images.

    Attributes:
        images (list[DiscoveryImageResponse]):
        count (int):
    """

    images: list[DiscoveryImageResponse]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "images": images,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_image_response import DiscoveryImageResponse

        d = dict(src_dict)
        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = DiscoveryImageResponse.from_dict(images_item_data)

            images.append(images_item)

        count = d.pop("count")

        discovery_image_list_response = cls(
            images=images,
            count=count,
        )

        discovery_image_list_response.additional_properties = d
        return discovery_image_list_response

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

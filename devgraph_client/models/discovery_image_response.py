from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.molecule_data import MoleculeData


T = TypeVar("T", bound="DiscoveryImageResponse")


@_attrs_define
class DiscoveryImageResponse:
    """Response for a discovery image.

    Attributes:
        id (UUID):
        image (str):
        tag (str):
        digest (None | str):
        description (None | str):
        is_default (bool):
        approved_by (None | str):
        approved_at (str):
        molecules (list[MoleculeData] | Unset): Molecules in this image
    """

    id: UUID
    image: str
    tag: str
    digest: None | str
    description: None | str
    is_default: bool
    approved_by: None | str
    approved_at: str
    molecules: list[MoleculeData] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        image = self.image

        tag = self.tag

        digest: None | str
        digest = self.digest

        description: None | str
        description = self.description

        is_default = self.is_default

        approved_by: None | str
        approved_by = self.approved_by

        approved_at = self.approved_at

        molecules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.molecules, Unset):
            molecules = []
            for molecules_item_data in self.molecules:
                molecules_item = molecules_item_data.to_dict()
                molecules.append(molecules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "image": image,
                "tag": tag,
                "digest": digest,
                "description": description,
                "is_default": is_default,
                "approved_by": approved_by,
                "approved_at": approved_at,
            }
        )
        if molecules is not UNSET:
            field_dict["molecules"] = molecules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.molecule_data import MoleculeData

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        image = d.pop("image")

        tag = d.pop("tag")

        def _parse_digest(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        digest = _parse_digest(d.pop("digest"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        is_default = d.pop("is_default")

        def _parse_approved_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved_by = _parse_approved_by(d.pop("approved_by"))

        approved_at = d.pop("approved_at")

        _molecules = d.pop("molecules", UNSET)
        molecules: list[MoleculeData] | Unset = UNSET
        if _molecules is not UNSET:
            molecules = []
            for molecules_item_data in _molecules:
                molecules_item = MoleculeData.from_dict(molecules_item_data)

                molecules.append(molecules_item)

        discovery_image_response = cls(
            id=id,
            image=image,
            tag=tag,
            digest=digest,
            description=description,
            is_default=is_default,
            approved_by=approved_by,
            approved_at=approved_at,
            molecules=molecules,
        )

        discovery_image_response.additional_properties = d
        return discovery_image_response

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

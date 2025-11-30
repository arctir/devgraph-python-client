from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_reference_response import EntityReferenceResponse
    from ..models.entity_relation_response_spec import EntityRelationResponseSpec
    from ..models.relation_metadata import RelationMetadata


T = TypeVar("T", bound="EntityRelationResponse")


@_attrs_define
class EntityRelationResponse:
    """
    Attributes:
        relation (str):
        source (EntityReferenceResponse):
        target (EntityReferenceResponse):
        namespace (str | Unset):  Default: 'default'.
        metadata (RelationMetadata | Unset): Metadata for a relation, following Kubernetes-style conventions.
        spec (EntityRelationResponseSpec | Unset):
    """

    relation: str
    source: EntityReferenceResponse
    target: EntityReferenceResponse
    namespace: str | Unset = "default"
    metadata: RelationMetadata | Unset = UNSET
    spec: EntityRelationResponseSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relation = self.relation

        source = self.source.to_dict()

        target = self.target.to_dict()

        namespace = self.namespace

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relation": relation,
                "source": source,
                "target": target,
            }
        )
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_reference_response import EntityReferenceResponse
        from ..models.entity_relation_response_spec import EntityRelationResponseSpec
        from ..models.relation_metadata import RelationMetadata

        d = dict(src_dict)
        relation = d.pop("relation")

        source = EntityReferenceResponse.from_dict(d.pop("source"))

        target = EntityReferenceResponse.from_dict(d.pop("target"))

        namespace = d.pop("namespace", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: RelationMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RelationMetadata.from_dict(_metadata)

        _spec = d.pop("spec", UNSET)
        spec: EntityRelationResponseSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = EntityRelationResponseSpec.from_dict(_spec)

        entity_relation_response = cls(
            relation=relation,
            source=source,
            target=target,
            namespace=namespace,
            metadata=metadata,
            spec=spec,
        )

        entity_relation_response.additional_properties = d
        return entity_relation_response

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

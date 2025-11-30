from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.molecule_data_config_schema_type_0 import MoleculeDataConfigSchemaType0


T = TypeVar("T", bound="MoleculeData")


@_attrs_define
class MoleculeData:
    """Molecule metadata from discovery pod.

    Attributes:
        name (str): Machine-readable molecule name
        version (str): Semantic version
        display_name (str): Human-readable name
        description (None | str | Unset):
        capabilities (list[str] | Unset): Capabilities like discovery, mcp
        entity_types (list[str] | Unset): Entity types created
        relation_types (list[str] | Unset): Relation types created
        requires_auth (bool | Unset): Whether auth is required Default: False.
        auth_types (list[str] | Unset): Supported auth types
        homepage_url (None | str | Unset):
        docs_url (None | str | Unset):
        deprecated (bool | Unset): Whether deprecated Default: False.
        replacement (None | str | Unset):
        config_schema (MoleculeDataConfigSchemaType0 | None | Unset):
        logo (Any | Unset):
    """

    name: str
    version: str
    display_name: str
    description: None | str | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    entity_types: list[str] | Unset = UNSET
    relation_types: list[str] | Unset = UNSET
    requires_auth: bool | Unset = False
    auth_types: list[str] | Unset = UNSET
    homepage_url: None | str | Unset = UNSET
    docs_url: None | str | Unset = UNSET
    deprecated: bool | Unset = False
    replacement: None | str | Unset = UNSET
    config_schema: MoleculeDataConfigSchemaType0 | None | Unset = UNSET
    logo: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.molecule_data_config_schema_type_0 import MoleculeDataConfigSchemaType0

        name = self.name

        version = self.version

        display_name = self.display_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        entity_types: list[str] | Unset = UNSET
        if not isinstance(self.entity_types, Unset):
            entity_types = self.entity_types

        relation_types: list[str] | Unset = UNSET
        if not isinstance(self.relation_types, Unset):
            relation_types = self.relation_types

        requires_auth = self.requires_auth

        auth_types: list[str] | Unset = UNSET
        if not isinstance(self.auth_types, Unset):
            auth_types = self.auth_types

        homepage_url: None | str | Unset
        if isinstance(self.homepage_url, Unset):
            homepage_url = UNSET
        else:
            homepage_url = self.homepage_url

        docs_url: None | str | Unset
        if isinstance(self.docs_url, Unset):
            docs_url = UNSET
        else:
            docs_url = self.docs_url

        deprecated = self.deprecated

        replacement: None | str | Unset
        if isinstance(self.replacement, Unset):
            replacement = UNSET
        else:
            replacement = self.replacement

        config_schema: dict[str, Any] | None | Unset
        if isinstance(self.config_schema, Unset):
            config_schema = UNSET
        elif isinstance(self.config_schema, MoleculeDataConfigSchemaType0):
            config_schema = self.config_schema.to_dict()
        else:
            config_schema = self.config_schema

        logo = self.logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "display_name": display_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if entity_types is not UNSET:
            field_dict["entity_types"] = entity_types
        if relation_types is not UNSET:
            field_dict["relation_types"] = relation_types
        if requires_auth is not UNSET:
            field_dict["requires_auth"] = requires_auth
        if auth_types is not UNSET:
            field_dict["auth_types"] = auth_types
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url
        if docs_url is not UNSET:
            field_dict["docs_url"] = docs_url
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if replacement is not UNSET:
            field_dict["replacement"] = replacement
        if config_schema is not UNSET:
            field_dict["config_schema"] = config_schema
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.molecule_data_config_schema_type_0 import MoleculeDataConfigSchemaType0

        d = dict(src_dict)
        name = d.pop("name")

        version = d.pop("version")

        display_name = d.pop("display_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        entity_types = cast(list[str], d.pop("entity_types", UNSET))

        relation_types = cast(list[str], d.pop("relation_types", UNSET))

        requires_auth = d.pop("requires_auth", UNSET)

        auth_types = cast(list[str], d.pop("auth_types", UNSET))

        def _parse_homepage_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        homepage_url = _parse_homepage_url(d.pop("homepage_url", UNSET))

        def _parse_docs_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docs_url = _parse_docs_url(d.pop("docs_url", UNSET))

        deprecated = d.pop("deprecated", UNSET)

        def _parse_replacement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replacement = _parse_replacement(d.pop("replacement", UNSET))

        def _parse_config_schema(data: object) -> MoleculeDataConfigSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_schema_type_0 = MoleculeDataConfigSchemaType0.from_dict(data)

                return config_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MoleculeDataConfigSchemaType0 | None | Unset, data)

        config_schema = _parse_config_schema(d.pop("config_schema", UNSET))

        logo = d.pop("logo", UNSET)

        molecule_data = cls(
            name=name,
            version=version,
            display_name=display_name,
            description=description,
            capabilities=capabilities,
            entity_types=entity_types,
            relation_types=relation_types,
            requires_auth=requires_auth,
            auth_types=auth_types,
            homepage_url=homepage_url,
            docs_url=docs_url,
            deprecated=deprecated,
            replacement=replacement,
            config_schema=config_schema,
            logo=logo,
        )

        molecule_data.additional_properties = d
        return molecule_data

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

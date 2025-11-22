from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_tools_response_tools import MCPToolsResponseTools


T = TypeVar("T", bound="MCPToolsResponse")


@_attrs_define
class MCPToolsResponse:
    """Response containing all MCP tools grouped by server.

    Attributes:
        tools (MCPToolsResponseTools):
        total_tools (int):
        total_endpoints (int):
        load_time (float | Unset):  Default: 0.0.
    """

    tools: MCPToolsResponseTools
    total_tools: int
    total_endpoints: int
    load_time: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tools = self.tools.to_dict()

        total_tools = self.total_tools

        total_endpoints = self.total_endpoints

        load_time = self.load_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tools": tools,
                "total_tools": total_tools,
                "total_endpoints": total_endpoints,
            }
        )
        if load_time is not UNSET:
            field_dict["load_time"] = load_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_tools_response_tools import MCPToolsResponseTools

        d = dict(src_dict)
        tools = MCPToolsResponseTools.from_dict(d.pop("tools"))

        total_tools = d.pop("total_tools")

        total_endpoints = d.pop("total_endpoints")

        load_time = d.pop("load_time", UNSET)

        mcp_tools_response = cls(
            tools=tools,
            total_tools=total_tools,
            total_endpoints=total_endpoints,
            load_time=load_time,
        )

        mcp_tools_response.additional_properties = d
        return mcp_tools_response

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

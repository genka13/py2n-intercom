"""Data models for py2n-intercom."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Py2NDeviceInfo:
    dev_type: str | None = None
    variant: str | None = None
    variant_id: int | None = None
    customer_id: int | None = None
    serial_number: str | None = None
    mac_addr: str | None = None
    hw_version: str | None = None
    sw_version: str | None = None
    build_type: str | None = None
    firmware_package: str | None = None
    device_name: str | None = None
    boot_uuid: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Py2NDeviceInfo":
        return cls(
            dev_type=data.get("devType"),
            variant=data.get("variant"),
            variant_id=data.get("variantId"),
            customer_id=data.get("customerId"),
            serial_number=data.get("serialNumber"),
            mac_addr=data.get("macAddr"),
            hw_version=data.get("hwVersion"),
            sw_version=data.get("swVersion"),
            build_type=data.get("buildType"),
            firmware_package=data.get("firmwarePackage"),
            device_name=data.get("deviceName"),
            boot_uuid=data.get("bootUuid"),
        )


@dataclass(frozen=True)
class Py2NLogEvent:
    event: str | None = None
    timestamp: str | None = None
    valid: bool | None = None
    params: dict[str, Any] | None = None
    raw: dict[str, Any] | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Py2NLogEvent":
        return cls(
            event=data.get("event"),
            timestamp=data.get("time") or data.get("timestamp"),
            valid=data.get("valid"),
            params=data.get("params") if isinstance(data.get("params"), dict) else None,
            raw=data,
        )


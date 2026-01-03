"""Data models for py2n-intercom.

These are intentionally small and stable, and represent the data the Home Assistant
integration needs for device registry and event processing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Py2NDeviceInfo:
    """Device identification and firmware details."""

    title: str | None = None
    model: str | None = None
    serial: str | None = None
    mac: str | None = None
    sw_version: str | None = None
    hw_version: str | None = None
    boot_uuid: str | None = None

    raw: dict[str, Any] | None = None


@dataclass(frozen=True)
class Py2NLogEvent:
    """Single event record returned by /api/log/pull."""

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


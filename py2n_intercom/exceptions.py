"""Exceptions for py2n-intercom."""

from __future__ import annotations


class Py2NApiError(Exception):
    """Raised on communication/auth errors with a 2N device."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status

    @property
    def is_unauthorized(self) -> bool:
        return str(self).lower() in {"unauthorized", "forbidden"} or self.status in {401, 403}


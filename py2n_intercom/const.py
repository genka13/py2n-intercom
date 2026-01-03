"""Constants for py2n-intercom.

This module is intentionally small and stable. API paths may evolve in the client,
but keeping them here helps reuse and testing.
"""

# Base API paths (2N HTTP API)
API_SYSTEM_INFO = "/api/system/info"

API_SWITCH_CAPS = "/api/switch/caps"
API_SWITCH_STATUS = "/api/switch/status"
API_SWITCH_CTRL = "/api/switch/ctrl"

API_CAMERA_CAPS = "/api/camera/caps"
API_CAMERA_SNAPSHOT = "/api/camera/snapshot"

API_LOG_CAPS = "/api/log/caps"
API_LOG_SUBSCRIBE = "/api/log/subscribe"
API_LOG_PULL = "/api/log/pull"
API_LOG_UNSUBSCRIBE = "/api/log/unsubscribe"

# Defaults (library-level)
DEFAULT_LOG_SUBSCRIBE_DURATION = 3600  # seconds
DEFAULT_LOG_PULL_TIMEOUT = 25  # seconds

DEFAULT_SNAPSHOT_WIDTH = 640
DEFAULT_SNAPSHOT_HEIGHT = 480

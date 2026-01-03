# py2n-intercom

Async Python client for the 2N IP intercom HTTP API (`/api/*`) and related RTSP endpoints.

This library is designed to be consumed by the Home Assistant `2n_intercom` integration, but can be used standalone.

## Supported devices / firmware

- 2N IP Style
- 2N IP Verso 2
- 2N IP One
- Firmware: **2.5+** (tested on 3.x)

## Install

```bash
pip install py2n-intercom
```

## Quick example

```python
import aiohttp
from py2n_intercom import Py2NClient

async def main():
    async with aiohttp.ClientSession() as session:
        client = Py2NClient(session, base_url="https://10.13.23.21", username="admin", password="***", auth_method="digest")
        info = await client.async_get_device_info()
        print(info)
```

## Development

Home Assistant developers can test the library in editable mode:

```bash
pip install -e .
```

Publish is expected to be automated via GitHub Actions on tags.

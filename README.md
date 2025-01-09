# Axis VAPIX Python API Handler

This project provides a Python-based API handler for interacting with [Axis](https://www.axis.com/) devices using the [VAPIX APIs](https://developer.axis.com/vapix).

---

## Features
- Easy interaction with Axis devices using VAPIX APIs.
- Support for synchronous and asynchronous requests.
- Prebuilt modules for device management, time settings, overlays, and more.

---

## Quick Start

Install the library:

```bash
pip install git+https://github.com/silvestrinigor/axis_vapix
```

### Example: Get Basic Device Information

```python
import requests
from axis.vapix.apis import basic_device_information

api_version = basic_device_information.ApiVersion(1, 0)
api_request = basic_device_information.RequestBasicDeviceInformation(host="192.168.0.90", port=80, api_version=api_version, context="test")

request = api_request.get_all_properties()
request.auth = requests.auth.HTTPBasicAuth("root", "pass")

with requests.Session() as session:
    response = session.send(request.prepare())

print(response.json())
```

---

## Installation

```bash
pip install git+https://github.com/silvestrinigor/axis_vapix
```

---

## Usage Examples

### 1. Set Time on Device

```python
import requests
from datetime import datetime
import pytz
from axis.vapix.apis import time_api

api_version = time_api.ApiVersion(1, 0)
api_request = time_api.RequestTimeApi(host="192.168.0.90", port=80, api_version=api_version)

timezone = pytz.timezone("America/Sao_Paulo")  # Use your time zone
date_time = datetime.now(timezone)

request = api_request.set_date_time(date_time)
request.auth = requests.auth.HTTPDigestAuth("root", "pass")

with requests.Session() as session:
    response = session.send(request.prepare())

print(response.json())
```

### 2. Add Text Overlay to Video

```python
import requests
from axis.vapix.apis import overlay_api

api_version = overlay_api.ApiVersion(1, 7)
api_request = overlay_api.RequestDynamicOverlayApi(host="192.168.0.90", port=80, api_version=api_version)

text_overlay = overlay_api.TextOverlay(camera=1, text="Hello, Axis!")

request = api_request.add_text(text_overlay)
request.auth = requests.auth.HTTPDigestAuth("root", "pass")

with requests.Session() as session:
    response = session.send(request.prepare())

print(response.json())
```

### 3. Asynchronous API Requests

```python
import aiohttp
from axis.vapix.apis import basic_device_information

async def main():
    api_version = basic_device_information.ApiVersion(1, 3)
    api = basic_device_information.BasicDeviceInformation(host="192.168.0.90", port=8000, api_version=api_version)

    async with aiohttp.ClientSession() as session:
        response = await api.get_all_properties_async(session, auth=aiohttp.BasicAuth("root", "pass"))
        print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Directory Structure

```bash
axis
├── __init__.py
└── vapix
    ├── __init__.py
    ├── apis
    │   ├── analytics_metadata_configuration.py
    │   ├── api_discovery_service.py
    │   ├── application_api.py
    │   ├── basic_device_information.py
    │   ├── firmware_management_api.py
    │   ├── loitering_guard.py
    │   ├── network_settings_api.py
    │   ├── ntp_api.py
    │   ├── object_analytics.py
    │   ├── overlay_api.py
    │   ├── parameter_management.py
    │   └── time_api.py
    ├── exceptions.py
    ├── handlers.py
    ├── interfaces.py
    ├── params.py
    ├── request.py
    ├── types.py
    └── utils.py
```

### Key Modules
- **`basic_device_information.py`**: Retrieve device information.
- **`time_api.py`**: Configure date and time on the device.
- **`overlay_api.py`**: Manage dynamic overlays (e.g., text, graphics).
- **`network_settings_api.py`**: Adjust network configurations.
- **`parameter_management.py`**: Handle general device parameters.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/silvestrinigor/axis_vapix).

---

## Support

For any issues or questions, please file a ticket on the [GitHub Issues page](https://github.com/silvestrinigor/axis_vapix/issues).


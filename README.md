# Axis VAPIX Python API Handler

This project provides a Python-based API handler for interacting with [Axis](https://www.axis.com/) devices using the [VAPIX APIs](https://developer.axis.com/vapix).

## Quick Start

Install the library:

```bash
pip install git+https://github.com/silvestrinigor/axis_vapix
```

### Example: Get Basic Device Information

```python
from axis.vapix import basic_device_information
import requests
import requests.auth

auth = requests.auth.HTTPDigestAuth("root", "pass")
api = basic_device_information.BasicDeviceInformationRequest("192.168.0.90", 80, auth)

request = api.getProperties([basic_device_information.DevicePropertyType.ARCHITECTURE, basic_device_information.DevicePropertyType.BRAND])

with requests.Session() as session:
    response = session.send(request.prepare())
    print(response.text)

# Output
{"apiVersion": "1.3", "data": {"propertyList": {"Brand": "AXIS", "Architecture": "armv7hf"}}}
```

---

### Example: Set Time

```python
from axis.vapix import time_api
import requests
import requests.auth
from datetime import datetime, timezone, timedelta

auth = requests.auth.HTTPDigestAuth("root", "pass")
api = time_api.TimeApiRequest("192.168.0.90", 80, auth)

time_now = datetime.now(timezone(timedelta(hours=-3)))
request = api.setDateTime(time_now)

with requests.Session() as session:
    response = session.send(request.prepare())
    print(response.text)

# Output
{
  "apiVersion": "1.0",
  "method": "setDateTime",
  "data": {
    "dateTime": "2025-04-09T15:51:39Z"
  }
}
```

---

## Supported APIs:
- Analytics Metadata Producer Configuration
- API Discovery service
- Basic device information
- Capture mode
- Firmware management API
- Loitering guard
- Network settings API
- NTP API
- AXIS Object analytics API
- Dynamic overlay API
- Time API

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/silvestrinigor/axis_vapix).

---

## Support

For any issues or questions, please file a ticket on the [GitHub Issues page](https://github.com/silvestrinigor/axis_vapix/issues).

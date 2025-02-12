# Axis VAPIX Python API Handler

This project provides a Python-based API handler for interacting with [Axis](https://www.axis.com/) devices using the [VAPIX APIs](https://developer.axis.com/vapix).

## Quick Start

Install the library:

```bash
pip install git+https://github.com/silvestrinigor/axis_vapix
```

### Example: Get Basic Device Information

```python
from axis import vapix
from axis.vapix.apis import BasicDeviceInformation

server = vapix.AxisServerInfo("192.168.0.90", "8000", "root", "pass")
api_version = vapix.ApiVersion(1,0)

with vapix.AxisSession(server, context="test") as session:
    api = BasicDeviceInformation(session, api_version)
    response = api.get_all_properties()

print(response.json())

# Output
{
  "apiVersion": "1.0",
  "context": "test",
  "data": {
  "propertyList": {
      "Archtecture": "mips",
      "Brand": "AXIS",
      "BuildDate": "Feb 14 2018 13:08",
      "HardwareID": "714.4",
      "ProdFullName": "AXIS Q3505 Mk II Fixed Dome Network Camera",
      "ProdNbr": "Q3505 Mk II",
      "ProdShortName": "AXIS Q3505 Mk II",
      "ProdType": "Network Camera",
      "ProdVariant": "",
      "SerialNumber": "ACCC8E78B977",
      "Soc": "Axis Artpec-5",
      "SocSerialNumber": "00000000-00000000-44123C08-C840037D",
      "Version": "8.20.1",
      "WebURL": "http://www.axis.com"
    }
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
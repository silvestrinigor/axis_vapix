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
from axis.vapix.apis import basic_device_information

server = vapix.AxisServer("192.168.0.90", "8000")
credencial = vapix.AxisCredencial("root", "pass")
api_version = vapix.ApiVersion(1,1)

with vapix.AxisSession(server, credencial, context="test") as session:
    bas_dev_info = basic_device_information.BasicDeviceInformation(session, api_version)
    response = bas_dev_info.get_all_properties()
    
print(response.json())

# Output
{
    "apiVersion": "1.3", 
    "data": {
        "propertyList": {
            ...        
        }
    }, 
    "context": "test"
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/silvestrinigor/axis_vapix).

---

## Support

For any issues or questions, please file a ticket on the [GitHub Issues page](https://github.com/silvestrinigor/axis_vapix/issues).
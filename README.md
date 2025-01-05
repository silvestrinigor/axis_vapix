# API Request for Axis VAPIX (Python)

## Overview

This project provides a Python-based API handler for interacting with Axis devices using the VAPIX APIs.

## Usage

```python
>>> import requests
>>> from axis.vapix.apis import basic_device_information
>>>
>>> api_version = basic_device_information.ApiVersion(1, 0)
>>> api_request = basic_device_information.RequestBasicDeviceInformation(host="192.168.0.90", port=80, api_version=api_version, context="test")
>>>
>>> request = api_request.get_all_properties()
>>> request.auth = requests.auth.HTTPBasicAuth("root", "pass")
>>> request_p = request.prepare()
>>>
>>> 
>>> with requests.Session() as session:
>>>     response = session.send(request_p)
>>> response.text
{
  "apiVersion": "1.0",
  "context": "test",
  "data": {
  "propertyList": {
    ... 
    }
  }
}
```

## Installation

```bash
$ pip install git+https://github.com/silvestrinigor/axis_vapix
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

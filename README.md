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

## Examples

- Set time
    ```python
    >>> import requests
    >>> import requests.auth
    >>> from axis.vapix.apis import time_api
    >>> 
    >>> api_version = time_api.ApiVersion(1,0)
    >>> api_request = time_api.RequestTimeApi(host="192.168.0.90", port="80", api_version=api_version)
    >>> 
    >>> from datetime import datetime
    >>> import pytz
    >>> 
    >>> timezone = pytz.timezone("America/Sao_Paulo") # use your time zone
    >>> date_time = datetime.now(timezone)
    >>> 
    >>> request = api_request.set_date_time(date_time)
    >>> request.auth = requests.auth.HTTPDigestAuth("root", "pass")
    >>> 
    >>> with requests.Session() as session:
    >>>     response = session.send(request.prepare())
    >>> 
    >>> response.text
    {
      "apiVersion": "1.0",
      "method": "setDateTime",
      "data": {
        "dateTime": "2025-01-07T16:36:25Z"
      }
    }
    ```
    
- Add text overlay
    ```python
    >>> import requests
    >>> import requests.auth
    >>> 
    >>> from axis.vapix.apis import overlay_api
    >>> 
    >>> api_version = overlay_api.ApiVersion(1,7)
    >>> api_request = overlay_api.RequestDynamicOverlayApi("192.168.0.90", 80, api_version)
    >>> 
    >>> text_overlay = overlay_api.TextOverlay(camera=1, text="test")
    >>> 
    >>> request = api_request.add_text(text_overlay)
    >>> request.auth = requests.auth.HTTPDigestAuth("root", "pass")
    >>> 
    >>> with requests.Session() as session:
    >>>     response = session.send(request.prepare())
    >>> 
    >>> response.text
    {
        "apiVersion": "1.7",
        "data": {
            "camera": 1,
            "identity": 2
        },
        "method": "addText"
    }
    ```
    

## License

This project is licensed under the MIT License. See the [LICENSE](/C:/Users/141669/AppData/Local/Programs/Joplin/resources/app.asar/LICENSE "LICENSE") file for details.
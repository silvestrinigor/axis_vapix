# API Request for Axis VAPIX (Python)

## Overview

This project provides a Python-based API handler for interacting with [Axis](https://www.axis.com/) devices using the [VAPIX APIs](https://developer.axis.com/vapix).

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

- Create and send a request to set time in device
    
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
    
- Create and send a request to add text overlay in device
    
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
    
- Get device info using async request
    
    ```python
    from axis.vapix.apis import basic_device_information
    import aiohttp
    
    async def main():
        api_version = basic_device_information.ApiVersion(1,3)
        api = basic_device_information.BasicDeviceInformation("192.168.0.90", "8000", api_version)
    
        async with aiohttp.ClientSession() as session:        
            content =  await api.get_all_properties_async(session, auth=aiohttp.BasicAuth("root", "pass"))
            print(content)
    
    if __name__ == '__main__':
        asyncio.run(main())
    
    #output
    """
    {
        'apiVersion': '1.3', 
        'data': {
        'propertyList': {
            ...
        }
    }
    """
    ```
    

## Tree

```bash
axix
├── __init__.py
└── vapix
    ├── __init__.py
    ├── apis
    │   ├── analytics_metadata_configuration.py
    │   ├── api_discovery_service.py
    │   ├── application_api.py
    │   ├── basic_device_information.py
    │   ├── firmware_management_api.py
    │   ├── loitering_guard.py
    │   ├── network_settings_api.py
    │   ├── ntp_api.py
    │   ├── object_analytics.py
    │   ├── overlay_api.py
    │   ├── parameter_management.py
    │   └── time_api.py
    ├── exeptions.py
    ├── handlers.py
    ├── interfaces.py
    ├── params.py
    ├── request.py
    ├── types.py
    └── utils.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](/C:/Users/141669/AppData/Local/Programs/Joplin/resources/app.asar/LICENSE "LICENSE") file for details.
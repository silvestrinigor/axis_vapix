# API Request for Axis VAPIX (Python)

## Overview

This project provides a Python-based API handler for interacting with Axis devices using the VAPIX APIs.

## Usage

```python
>>> import requests
>>> import axis.vapix
>>> import axis.vapix.apis

>>> api_request = axis.vapix.apis.RequestBasicDeviceInformation(host="192.168.0.90", port=80, "1.0", context="test")
>>> request = api_request.get_all_properties()
>>> request.auth = requests.auth.HTTPBasicAuth("root", "pass")
>>> request_p = request.prepare()
>>> response = requests.Session().send(request_p)
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

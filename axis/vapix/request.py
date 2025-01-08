import aiohttp
import requests

class AxisRequest(requests.Request):
    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)


class AxisVapixSession(requests.Session):
    def __init__(self):
        super().__init__()

class AxisVapixAsyncSession(aiohttp.ClientSession):
    def __init__(self):
        super().__init__()
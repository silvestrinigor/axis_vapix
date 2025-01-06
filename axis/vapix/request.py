from aiohttp import ClientRequest, http
from requests import Request

class AxisRequest(Request):
    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)

class AxisRequestAsync(ClientRequest):
    def __init__(self, method, url, *, params = None, headers = None, skip_auto_headers = None, data = None, cookies = None, auth = None, version = http.HttpVersion11, compress = None, chunked = None, expect100 = False, loop = None, response_class = None, proxy = None, proxy_auth = None, timer = None, session = None, ssl = True, proxy_headers = None, traces = None, trust_env = False, server_hostname = None):
        super().__init__(method, url, params=params, headers=headers, skip_auto_headers=skip_auto_headers, data=data, cookies=cookies, auth=auth, version=version, compress=compress, chunked=chunked, expect100=expect100, loop=loop, response_class=response_class, proxy=proxy, proxy_auth=proxy_auth, timer=timer, session=session, ssl=ssl, proxy_headers=proxy_headers, traces=traces, trust_env=trust_env, server_hostname=server_hostname)
        
        

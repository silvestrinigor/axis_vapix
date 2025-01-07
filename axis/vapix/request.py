from aiohttp import ClientRequest, http, ClientSession
from requests import Request, Session
import json

class AxisRequest(Request):
    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)

class AxisRequestAsync(ClientRequest):
    def __init__(self, method, url, *, params = None, headers = None, skip_auto_headers = None, data = None, cookies = None, auth = None, version = http.HttpVersion11, compress = None, chunked = None, expect100 = False, loop = None, response_class = None, proxy = None, proxy_auth = None, timer = None, session = None, ssl = True, proxy_headers = None, traces = None, trust_env = False, server_hostname = None):
        super().__init__(method, url, params=params, headers=headers, skip_auto_headers=skip_auto_headers, data=data, cookies=cookies, auth=auth, version=version, compress=compress, chunked=chunked, expect100=expect100, loop=loop, response_class=response_class, proxy=proxy, proxy_auth=proxy_auth, timer=timer, session=session, ssl=ssl, proxy_headers=proxy_headers, traces=traces, trust_env=trust_env, server_hostname=server_hostname)
        
class AxisVapixSession(Session):
    def __init__(self):
        super().__init__()
        
class AxisVapixAsyncSession(ClientSession):
    def __init__(self, base_url=None, *, connector=None, loop=None, cookies=None, headers=None, proxy=None, 
                 proxy_auth=None, skip_auto_headers=None, auth=None, json_serialize=json.dumps, 
                 request_class=None, response_class=None, ws_response_class=None, version=http.HttpVersion11, 
                 cookie_jar=None, connector_owner=True, raise_for_status=False, read_timeout=None, conn_timeout=None, 
                 timeout=None, auto_decompress=True, trust_env=False, requote_redirect_url=True, trace_configs=None, 
                 read_bufsize=2**16, max_line_size=8190, max_field_size=8190, fallback_charset_resolver=None):

        super().__init__(base_url=base_url, connector=connector, loop=loop, cookies=cookies, headers=headers, 
                         proxy=proxy, proxy_auth=proxy_auth, skip_auto_headers=skip_auto_headers, auth=auth, 
                         json_serialize=json_serialize, request_class=request_class, response_class=response_class, 
                         ws_response_class=ws_response_class, version=version, cookie_jar=cookie_jar, 
                         connector_owner=connector_owner, raise_for_status=raise_for_status, read_timeout=read_timeout, 
                         conn_timeout=conn_timeout, timeout=timeout, auto_decompress=auto_decompress, trust_env=trust_env, 
                         requote_redirect_url=requote_redirect_url, trace_configs=trace_configs, 
                         read_bufsize=read_bufsize, max_line_size=max_line_size, max_field_size=max_field_size, 
                         fallback_charset_resolver=fallback_charset_resolver)
    
    async def axis_request(self, request: AxisRequestAsync):
        # Get values from AxisRequestAsync (or fall back to defaults)
        method = request.method
        url = request.url
        params = request.params
        headers = request.headers or self.headers  # Fallback to session headers
        skip_auto_headers = request.skip_auto_headers
        data = request.data
        cookies = request.cookies
        auth = request.auth
        version = request.version
        compress = request.compress
        chunked = request.chunked
        expect100 = request.expect100
        loop = request.loop or self._loop
        response_class = request.response_class or self.response_class
        proxy = request.proxy
        proxy_auth = request.proxy_auth
        timer = request.timer
        session = request.session
        ssl = request.ssl
        proxy_headers = request.proxy_headers
        traces = request.traces
        trust_env = request.trust_env
        server_hostname = request.server_hostname

        # Call the super method (ClientSession.request)
        return await super().request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            skip_auto_headers=skip_auto_headers,
            data=data,
            cookies=cookies,
            auth=auth,
            version=version,
            compress=compress,
            chunked=chunked,
            expect100=expect100,
            loop=loop,
            response_class=response_class,
            proxy=proxy,
            proxy_auth=proxy_auth,
            timer=timer,
            session=session,
            ssl=ssl,
            proxy_headers=proxy_headers,
            traces=traces,
            trust_env=trust_env,
            server_hostname=server_hostname
        )

from abc import ABC
from .request import AxisRequest, AxisVapixSession, AxisVapixAsyncSession
from .handlers import AxisVapixResponseHandler, AxisVapixAsyncResponseHandler
from .types import ApiPathType, MethodType, RequestParamType
from .params import ApiVersion

class IRequestAxisVapix(ABC):
    def __init__(self, host: str, port: int, api_version: ApiVersion | None = None, context: str | None = None):
        self._host = host
        self._port = port
        self._api_version = api_version
        self._api_path_type = ApiPathType.NONE
        self._context = context

    def _get_basic_request_body(self):
        request_body = {}
        if self._api_version != None: request_body[RequestParamType.API_VERSION.value] = str(self._api_version)
        if self._context != None: request_body[RequestParamType.CONTEXT.value] = self._context 
        return request_body

    def _get_supported_versions(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
        if self._api_path_type.value == None: 
            raise ValueError("API path type is not set")
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def _create_request(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        return AxisRequest(method, url, headers, files, data, params, auth, cookies, hooks, json)

    def _send_request(self, request: AxisRequest, session: AxisVapixSession):
        request.prepare()
        response = session.send(request)
        AxisVapixResponseHandler(response)
        return response.json()
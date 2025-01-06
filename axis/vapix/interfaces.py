from abc import ABC
from .request import AxisRequest
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
        if self._api_version != None: request_body[RequestParamType.API_VERSION.value] = self._api_version
        if self._context != None: request_body[RequestParamType.CONTEXT.value] = self._context 
        return request_body

    def _get_supported_versions(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_VERSIONS.value
        if self._api_path_type.value == None: 
            raise ValueError("API path type is not set")
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)


from .apis import RequestAxisVapix
from .types import ApiPathType, RequestParamType, MethodType
from requests import Request

class RequestApiDiscoveryService(RequestAxisVapix):
    """
    Firmware: 8.50 and later
    Property: Properties.ApiDiscovery.ApiDiscovery="yes"
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_API_DISCOVERY

    def get_api_list(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_API_LIST.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

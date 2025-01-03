"""
https://developer.axis.com/vapix/network-video/api-discovery-service
"""

from ..request import AxisRequest
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType
from ..params import ApiVersion, FirmwareVersion

API_DISCOVERY_SERVICE_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 50, 0)

class RequestApiDiscoveryService(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_API_DISCOVERY

    def get_api_list(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_API_LIST.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

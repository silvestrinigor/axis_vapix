"""
https://developer.axis.com/vapix/network-video/api-discovery-service
"""

from enum import Enum
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApi
from ..requests import AxisSession

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 50, 0)
PATH = "axis-cgi/apidiscovery.cgi"
REQUEST_METHOD = "POST"


PROPERTIES = [
    "Properties.ApiDiscovery.ApiDiscovery=yes"
]


BODY = {
    "apiVersion": None,
    "context": None,
    "method": None
}


class MethodType(Enum):
    GET_API_LIST = "getApiList"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


class ApiDiscoveryService(IVapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH)

    def get_api_list(self):
        body = self._create_body(MethodType.GET_API_LIST)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
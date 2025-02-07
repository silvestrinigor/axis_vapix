"""
https://developer.axis.com/vapix/network-video/api-discovery-service
"""

from enum import Enum
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApiClass
from ..requests import VapixRequest, AxisSession
from .. import utils

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 50, 0)
PATH = "axis-cgi/apidiscovery.cgi"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None
}


class MethodType(Enum):
    GET_API_LIST = "getApiList"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


class ApiDiscoveryService(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)

    def get_api_list(self):
        body = self._create_body(MethodType.GET_API_LIST)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def _create_request(self, json: dict):
        request = VapixRequest(
            method=REQUEST_METHOD, 
            url=self._base_url + PATH, 
            json=json, 
            auth=self.session.auth_type.value(
                self.session.credencial.username, 
                self.session.credencial.password
                )
            )
        return request
    
    def _create_body(self, method: MethodType, params: dict | None = None):
        body = BODY
        body["apiVersion"] = str(self.api_version)
        body["context"] = self.session.context
        body["method"] = method.value
        body["params"] = params
        body = utils.remove_none_values(body)
        return body
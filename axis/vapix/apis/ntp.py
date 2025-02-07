"""
https://developer.axis.com/vapix/network-video/ntp-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApiClass
from ..requests import VapixRequest, AxisSession
from .. import utils

PATH = "axis-cgi/ntp.cgi"
LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(9, 10, 0)
DISCOVERY_API_ID = "ntp"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}

class MethodType(Enum):
    GET_NTP_INFO = "getNTPInfo"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    SET_NTP_CLIENT_CONFIGURATION = "setNTPClientConfiguration"


class ServersSourceType(Enum):
    DHCP = "DHCP"
    STATIC = "static"
    NONE = None


@dataclass
class NTPClientConfiguration:
    enable: bool | None = None
    ntsEnable: bool | None = None
    serversSource: ServersSourceType | None = None
    staticServersList: list[str] | None = None
    staticNtskeServersList: list[str] | None = None


class NtpApi(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)
    
    def get_ntp_info(self):
        body = self._create_body(MethodType.GET_NTP_INFO)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def set_ntp_client_configuration(self, configuration: NTPClientConfiguration): 
        params = asdict(configuration)
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS, params)
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
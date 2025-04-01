"""
https://developer.axis.com/vapix/network-video/ntp-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..connection import ApiVersion, FirmwareVersion
from ..abc import VapixApi
from ..requests import AxisSession

PATH = "axis-cgi/ntp.cgi"
LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(9, 10, 0)
DISCOVERY_API_ID = "ntp"
REQUEST_METHOD = "POST"


PROPERTIES = [
    "Properties.API.HTTP.Version=3"
]


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


class NtpApi(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)
    
    def get_ntp_info(self):
        body = self._create_body(MethodType.GET_NTP_INFO)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_ntp_client_configuration(self, configuration: NTPClientConfiguration): 
        params = asdict(configuration)
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
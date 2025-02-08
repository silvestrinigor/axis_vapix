"""
https://developer.axis.com/vapix/network-video/basic-device-information
"""
from enum import Enum
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApi
from ..requests import AxisSession

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 40, 0)
DISCOVERY_API_ID = "basic-device-info"
PATH = "axis-cgi/basicdeviceinfo.cgi"
REQUEST_METHOD = "POST"


PROPERTIES = [
    "BasicDeviceInfo.BasicDeviceInfo=yes"
]


BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}


class DevicePropertyType(Enum):
    ARCHITECTURE = "Architecture"
    BRAND = "Brand"
    BUILD_DATE = "BuildDate"
    HARDWARE_ID = "hardwareId"
    PROD_FULL_NAME = "ProdFullName"
    PROD_NBR = "ProdNbr"
    PROD_SHORT_NAME = "ProdShortName"
    PROD_TYPE = "ProdType"
    PROD_VARIANT = "ProdVariant"
    SERIAL_NUMBER = "SerialNumber"
    SOC = "Soc"
    SOC_SERIAL_NUMBER = "SocSerialNumber"
    VERSION = "Version"
    WEB_URL = "WebURL"


class MethodType(Enum):
    GET_PROPERTIES = "getProperties"
    GET_ALL_PROPERTIES = "getAllProperties"
    GET_ALL_UNRESTRICTED_PROPERTIES = "getAllUnrestrictedProperties"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


class BasicDeviceInformation(IVapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH)
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {"propertyList": [prop.value for prop in properties]}
        body = self._create_body(MethodType.GET_PROPERTIES, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_all_properties(self):
        body = self._create_body(MethodType.GET_ALL_PROPERTIES)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_all_unrestricted_properties(self):
        body = self._create_body(MethodType.GET_ALL_UNRESTRICTED_PROPERTIES)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
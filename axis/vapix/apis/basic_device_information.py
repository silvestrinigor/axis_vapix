"""
https://developer.axis.com/vapix/network-video/basic-device-information
"""
from enum import Enum
from ..api import IVapixApiClass, FirmwareVersion, ApiVersion
from ..requests import VapixRequest, AxisSession
from .. import utils

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 40, 0)
DISCOVERY_API_ID = "basic-device-info"
PATH = "axis-cgi/basicdeviceinfo.cgi"
REQUEST_METHOD = "POST"

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


class BasicDeviceInformation(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {"propertyList": [prop.value for prop in properties]}
        body = self._create_body(MethodType.GET_PROPERTIES, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def get_all_properties(self):
        body = self._create_body(MethodType.GET_ALL_PROPERTIES)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def get_all_unrestricted_properties(self):
        body = self._create_body(MethodType.GET_ALL_UNRESTRICTED_PROPERTIES)
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


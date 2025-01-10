"""
https://developer.axis.com/vapix/network-video/basic-device-information
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, DevicePropertyType, ParamType, RequestParamType, MethodType
from ..params import ApiVersion, FirmwareVersion
from .. import request

BASIC_DEVICE_INFORMATION_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 40, 0)
BASIC_DEVICE_INFORMATION_API_DISCOVERY_API_ID = "basic-device-info"

class RequestBasicDeviceInformation(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_PROPERTIES.value
        request_body[RequestParamType.PARAMS.value] = params
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_PROPERTIES.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_unrestricted_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_UNRESTRICTED_PROPERTIES.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class BasicDeviceInformation(RequestBasicDeviceInformation):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)
    
    def get_properties(self, properties: list[DevicePropertyType], session: request.AxisVapixSession, auth):
        request = super().get_properties(properties)
        request.auth = auth
        self._send_request(request, session)
    
    def get_all_properties(self, session: request.AxisVapixSession, auth):
        request = super().get_all_properties()
        request.auth = auth
        self._send_request(request, session)
    
    def get_all_unrestricted_properties(self, session: request.AxisVapixSession, auth):
        request = super().get_all_unrestricted_properties()
        request.auth = auth
        self._send_request(request, session)

    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)


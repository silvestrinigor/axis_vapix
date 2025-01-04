"""
https://developer.axis.com/vapix/network-video/basic-device-information
"""

from requests import Request
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, DevicePropertyType, ParamType, RequestParamType, MethodType
from ..params import ApiVersion

class RequestBasicDeviceInformation(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_BASIC_DEVICE_INFO
    
    def get_properties(self, properties: list[DevicePropertyType]):
        params = {ParamType.PROPERTY_LIST.value: [prop.value for prop in properties]}
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_PROPERTIES.value
        request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_PROPERTIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_all_unrestricted_properties(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL_UNRESTRICTED_PROPERTIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

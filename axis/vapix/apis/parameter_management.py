"""
https://developer.axis.com/vapix/network-video/parameter-management
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, ActionType, RequestUrlParamType
from ..params import FirmwareVersion

PARAMETER_MANAGEMENT_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(5, 0, 0)

class RequestParameterManagement(IRequestAxisVapix):

    def __init__(self, host: str, port: int, context: str | None = None):
        super().__init__(host, port, context)
        self._api_path_type = ApiPathType.AXIS_CGI_PARAM
    
    def list(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.LIST.value}{uri}")
        return request

    def list_definitions(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.LIST_DEFINITIONS.value}{uri}")
        return request
    
    def update(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.UPDATE.value}{uri}")
        return request
    
    def add(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.ADD.value}{uri}")
        return request
    
    def remove(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.REMOVE.value}{uri}")
        return request
    
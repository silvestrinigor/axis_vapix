"""
https://developer.axis.com/vapix/network-video/parameter-management
"""

from ..request import AxisRequest
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, ActionType, RequestUrlParamType
from ..params import FirmwareVersion

PARAMETER_MANAGEMENT_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(5, 0, 0)

class RequestParameterManagement(IRequestAxisVapix):

    def __init__(self, host: str, port: int, context: str | None = None):
        super().__init__(host, port, context)
        self._api_path_type = ApiPathType.AXIS_CGI_PARAM

    def get_request(self, action: ActionType, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        if action == ActionType.LIST:
            request_method = "GET"
        else:
            request_method = "POST"
        request = AxisRequest(request_method, f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{action.value}{uri}")
        return request

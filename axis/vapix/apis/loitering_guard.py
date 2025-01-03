"""
https://developer.axis.com/vapix/applications/loitering-guard
"""

from ..request import AxisRequest
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import ApiVersion, LoiteringGuardConfiguration

class RequestLoiteringGuard(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.LOCAL_LOITERING_GUARD
    
    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_configuration(self, configuration: LoiteringGuardConfiguration):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_CONFIGURATION.value
        request_body[RequestParamType.PARAMS.value] = configuration.get_all_params()
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def send_alarm(self, profile: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SEND_ALARM_EVENT.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PROFILE.value: profile}
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION_CAPABILITIES.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

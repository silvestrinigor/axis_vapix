"""
https://developer.axis.com/vapix/applications/axis-object-analytics-api
"""

from requests import Request
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import ApiVersion

class RequestObjectAnalyticsApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.LOCAL_OBJECT_ANALYTICS

    def get_configuration_capabilities(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION_CAPABILITIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def send_alarm(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SEND_ALARM.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_accumulated_count(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ACCUMULATED_COUNTS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def reset_accumulated_counts(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.RESET_ACCUMULATED_COUNTS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def reset_passthrough(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.RESET_PASSTHROUGH.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_occupancy(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_OCCUPANCY.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()
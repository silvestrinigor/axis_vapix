"""
https://developer.axis.com/vapix/applications/axis-object-analytics-api
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import ApiVersion, ObjectAnalyticsConfiguration
from .. import request

class RequestObjectAnalyticsApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.LOCAL_OBJECT_ANALYTICS

    def get_configuration_capabilities(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION_CAPABILITIES.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_configuration(self, configuration: ObjectAnalyticsConfiguration):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_CONFIGURATION.value
        request_body[RequestParamType.PARAMS.value] = configuration.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def send_alarm(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SEND_ALARM.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_accumulated_count(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ACCUMULATED_COUNTS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def reset_accumulated_counts(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.RESET_ACCUMULATED_COUNTS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def reset_passthrough(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.RESET_PASSTHROUGH.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_occupancy(self, scenario: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_OCCUPANCY.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.SCENARIO.value: scenario}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()
    
class ObjectAnalyticsApi(RequestObjectAnalyticsApi):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)

    def get_configuration_capabilities(self, session: request.AxisVapixSession, auth):
        request = super().get_configuration_capabilities()
        request.auth = auth
        self._send_request(request, session)

    def get_configuration(self, session: request.AxisVapixSession, auth):
        request = super().get_configuration()
        request.auth = auth
        self._send_request(request, session)

    def set_configuration(self, configuration: ObjectAnalyticsConfiguration, session: request.AxisVapixSession, auth):
        request = super().set_configuration(configuration)
        request.auth = auth
        self._send_request(request, session)

    def send_alarm(self, scenario: int, session: request.AxisVapixSession, auth):
        request = super().send_alarm(scenario)
        request.auth = auth
        self._send_request(request, session)

    def get_accumulated_count(self, scenario: int, session: request.AxisVapixSession, auth):
        request = super().get_accumulated_count(scenario)
        request.auth = auth
        self._send_request(request, session)

    def reset_accumulated_counts(self, scenario: int, session: request.AxisVapixSession, auth):
        request = super().reset_accumulated_counts(scenario)
        request.auth = auth
        self._send_request(request, session)

    def reset_passthrough(self, scenario: int, session: request.AxisVapixSession, auth):
        request = super().reset_passthrough(scenario)
        request.auth = auth
        self._send_request(request, session)

    def get_occupancy(self, scenario: int, session: request.AxisVapixSession, auth):
        request = super().get_occupancy(scenario)
        request.auth = auth
        self._send_request(request, session)

    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)

    async def get_configuration_capabilities_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_configuration_capabilities()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def get_configuration_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_configuration()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def set_configuration_async(self, configuration: ObjectAnalyticsConfiguration, session: request.AxisVapixAsyncSession, auth):
        request = super().set_configuration(configuration)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def send_alarm_async(self, scenario: int, session: request.AxisVapixAsyncSession, auth):
        request = super().send_alarm(scenario)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def get_accumulated_count_async(self, scenario: int, session: request.AxisVapixAsyncSession, auth):
        request = super().get_accumulated_count(scenario)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def reset_accumulated_counts_async(self, scenario: int, session: request.AxisVapixAsyncSession, auth):
        request = super().reset_accumulated_counts(scenario)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
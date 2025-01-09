"""
https://developer.axis.com/vapix/applications/loitering-guard
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import ApiVersion, LoiteringGuardConfiguration
from .. import request

class RequestLoiteringGuard(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.LOCAL_LOITERING_GUARD
    
    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_configuration(self, configuration: LoiteringGuardConfiguration):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_CONFIGURATION.value
        request_body[RequestParamType.PARAMS.value] = configuration.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def send_alarm(self, profile: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SEND_ALARM_EVENT.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PROFILE.value: profile}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_configuration_capabilities(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION_CAPABILITIES.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class LoiteringGuard(RequestLoiteringGuard):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)
        
    def get_configuration(self, session: request.AxisVapixSession, auth):
        request = super().get_configuration()
        request.auth = auth
        self._send_request(request, session)
        
    def set_configuration(self, configuration: LoiteringGuardConfiguration, session: request.AxisVapixSession, auth):
        request = super().set_configuration(configuration)
        request.auth = auth
        self._send_request(request, session)
        
    def send_alarm(self, profile: int, session: request.AxisVapixSession, auth):
        request = super().send_alarm(profile)
        request.auth = auth
        self._send_request(request, session)
        
    def get_configuration_capabilities(self, session: request.AxisVapixSession, auth):
        request = super().get_configuration_capabilities()
        request.auth = auth
        self._send_request(request, session)

    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)

    async def get_configuration_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_configuration()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def set_configuration_async(self, configuration: LoiteringGuardConfiguration, session: request.AxisVapixAsyncSession, auth):
        request = super().set_configuration(configuration)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def send_alarm_async(self, profile: int, session: request.AxisVapixAsyncSession, auth):
        request = super().send_alarm(profile)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def get_configuration_capabilities_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_configuration_capabilities()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def get_supported_versions_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
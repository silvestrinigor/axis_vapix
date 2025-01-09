"""
https://developer.axis.com/vapix/network-video/ntp-api
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, MethodType, RequestParamType
from ..params import ApiVersion, NTPClientConfiguration, FirmwareVersion
from .. import request

NTP_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(9, 10, 0)
NTP_API_DISCOVERY_API_ID = "ntp"

class RequestNtpApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_NTP
        
    def get_ntp_info(self): 
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_NTP_INFO.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_ntp_client_configuration(self, ntp_client_configuration: NTPClientConfiguration): 
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_NTP_CLIENT_CONFIGURATION.value
        request_body[RequestParamType.PARAMS.value] = ntp_client_configuration.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class NtpApi(RequestNtpApi):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)

    def get_ntp_info(self, session: request.AxisVapixSession, auth):
        request = super().get_ntp_info()
        request.auth = auth
        self._send_request(request, session)

    def set_ntp_client_configuration(self, ntp_client_configuration: NTPClientConfiguration, session: request.AxisVapixSession, auth):
        request = super().set_ntp_client_configuration(ntp_client_configuration)
        request.auth = auth
        self._send_request(request, session)

    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)

    async def get_ntp_info_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_ntp_info()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def set_ntp_client_configuration_async(self, ntp_client_configuration: NTPClientConfiguration, session: request.AxisVapixAsyncSession, auth):
        request = super().set_ntp_client_configuration(ntp_client_configuration)
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
    
    async def get_supported_versions_async(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        return await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
"""
https://developer.axis.com/vapix/network-video/analytics-metadata-producer-configuration
"""

from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import AnalyticsMetadataProducer, ApiVersion
from ..interfaces import IRequestAxisVapix
from ..handlers import AxisVapixAsyncResponseHandler
from .. import request

ANALYTICS_METADATA_PRODUCER_CONFIGURATION_DISCOVERY_API_ID = "analytics-metadata-config"

class RequestAnalyticsMetadataProducerConfiguration(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_ANALYTICS_METADATA_CONFIG

    def list_producers(self, producers: list[str]):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.LIST_PRODUCERS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def set_enable_producers(self, producers: list[AnalyticsMetadataProducer]):
        producers = {}
        for producer in producers:
            producers.append(producer.get_all_params())
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_ENABLED_PRODUCERS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def get_supported_metadata(self, producers: list[str]):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_METADATA.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json=request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

class AnalyticsMetadataProducerConfiguration(RequestAnalyticsMetadataProducerConfiguration):
    def __init__(self, host, port, api_version, context=None):
        super().__init__(host, port, api_version, context)
        
    def list_producers(self, producers: list[str], session: request.AxisVapixSession, auth):
        request = super().list_producers(producers)
        request.auth = auth
        self._send_request(request, session)
    
    def set_enable_producers(self, producers: list[str], session: request.AxisVapixSession, auth):
        request = super().set_enable_producers(producers)
        request.auth = auth
        self._send_request(request, session)
        
    def get_supported_metadata(self, producers: list[str], session: request.AxisVapixSession, auth):
        request = super().get_supported_metadata(producers)
        request.auth = auth
        self._send_request(request, session)
        
    def get_supported_versions(self, session: request.AxisVapixSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        self._send_request(request, session)

    async def async_list_producers(self, producers: list[str], session: request.AxisVapixAsyncSession, auth):
        request = super().list_producers(producers)
        request.auth = auth
        response = await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response

    async def async_set_enable_producers(self, producers: list[str], session: request.AxisVapixAsyncSession, auth):
        request = super().set_enable_producers(producers)
        request.auth = auth
        response = await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response

    async def async_get_supported_metadata(self, producers: list[str], session: request.AxisVapixAsyncSession, auth):
        request = super().get_supported_metadata(producers)
        request.auth = auth
        response = await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response

    async def async_get_supported_versions(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_supported_versions()
        request.auth = auth
        response = await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
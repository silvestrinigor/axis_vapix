from .apis import RequestAxisVapix
from .types import ApiPathType, RequestParamType, MethodType, ParamType
from .defaults import AnalyticsMetadataProducer
from requests import Request

class RequestAnalyticsMetadataProducerConfiguration(RequestAxisVapix):
    """
    API Discovery: id=analytics-metadata-config
    """
    def __init__(self, host: str, port: int, api_version: str, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_ANALYTICS_METADATA_CONFIG

    def list_producers(self, producers: list[str]):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.LIST_PRODUCERS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_enable_producers(self, producers: list[AnalyticsMetadataProducer]):
        producers = {}
        for producer in producers:
            producers.append(producer.get_all_params())
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_ENABLED_PRODUCERS.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_metadata(self, producers: list[str]):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_SUPPORTED_METADATA.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PRODUCERS.value: producers}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

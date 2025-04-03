"""
https://developer.axis.com/vapix/network-video/analytics-metadata-producer-configuration
"""

from dataclasses import dataclass, asdict
from enum import Enum
from .connection import ApiVersion
from .abc import VapixApi
from .requests import AxisSession

DISCOVERY_API_ID = "analytics-metadata-config"
PATH = "axis-cgi/analyticsmetadataconfig.cgi"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}


class MethodType(Enum):
    LIST_PRODURERS = "listProducers"
    SET_ENABLE_PRODUCERS = "setEnabledProducers"
    GET_SUPPORTED_METADATA = "getSupportedMetadata"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


@dataclass
class AnalyticsMetadataVideoChannel:
    channel: int | None = None
    enabled: bool | None = None


@dataclass
class AnalyticsMetadataProducer:
    name: str | None = None
    videoChannels: list[AnalyticsMetadataVideoChannel] | None = None


class AnalyticsMetadataProducerConfiguration(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)

    def list_producers(self, producers: list[str] | None = None):
        params = None
        if producers != None:
            params = {"producers": producers}
        body = self._create_body(MethodType.LIST_PRODURERS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_enable_producers(self, producers: list[AnalyticsMetadataProducer]):
        producers_dict = []
        for producer in producers:
            producers_dict.append(asdict(producer))
        params = {"producers": producers_dict}
        body = self._create_body(MethodType.SET_ENABLE_PRODUCERS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_supported_metadata(self, producers: list[str] | None = None):
        params = None
        if producers != None:
            params = {"producers": producers}
        body = self._create_body(MethodType.GET_SUPPORTED_METADATA, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
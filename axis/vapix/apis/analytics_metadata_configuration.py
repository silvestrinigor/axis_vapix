"""
https://developer.axis.com/vapix/network-video/analytics-metadata-producer-configuration
"""

from dataclasses import dataclass, asdict
from enum import Enum
from ..api import IVapixApiClass, ApiVersion
from ..requests import VapixRequest, AxisSession
from .. import utils

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


class AnalyticsMetadataProducerConfiguration(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)

    def list_producers(self, producers: list[str] | None = None):
        params = None
        if producers != None:
            params = {"producers": producers}
        body = self._create_body(MethodType.LIST_PRODURERS, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def set_enable_producers(self, producers: list[AnalyticsMetadataProducer]):
        producers_dict = []
        for producer in producers:
            producers_dict.append(asdict(producer))
        params = {"producers": producers_dict}
        body = self._create_body(MethodType.SET_ENABLE_PRODUCERS, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def get_supported_metadata(self, producers: list[str] | None = None):
        params = None
        if producers != None:
            params = {"producers": producers}
        body = self._create_body(MethodType.GET_SUPPORTED_METADATA, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def _create_request(self, json: dict):
        request = VapixRequest(
            method=REQUEST_METHOD, 
            url=self._base_url + PATH, 
            json=json, 
            auth=self.session.auth_type.value(
                self.session.credencial.username, 
                self.session.credencial.password
                )
            )
        return request
    
    def _create_body(self, method: MethodType, params: dict | None = None):
        body = BODY
        body["apiVersion"] = str(self.api_version)
        body["context"] = self.session.context
        body["method"] = method.value
        body["params"] = params
        body = utils.remove_none_values(body)
        return body
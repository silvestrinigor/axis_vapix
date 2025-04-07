from requests import Request
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from .requests import VapixApiRequest
from .api import VapixApiABC

@dataclass
class AnalyticsMetadataVideoChannel:
    channel: int | None = None
    enabled: bool | None = None

@dataclass
class AnalyticsMetadataProducer:
    name: str | None = None
    videoChannels: list[AnalyticsMetadataVideoChannel] | None = None

class AnalyticsMetadataProducerConfigurationABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/analyticsmetadataconfig.cgi"
    API_DISCOVERY_ID = "analytics-metadata-config"
    
    @abstractmethod
    def listProducers(self, producers: list[str] | None = None):
        pass
    
    @abstractmethod
    def setEnableProducers(self, producers: list[dict] | list[AnalyticsMetadataProducer]):
        pass
    
    @abstractmethod
    def getSupportedMetadata(self, producers: list[str] | None = None):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
class AnalyticsMetadataProducerConfigurationRequest(AnalyticsMetadataProducerConfigurationABC, VapixApiRequest):
    
    def listProducers(self, producers: list[str] | None = None):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "listProducers",
        }
        
        params = {}
        if producers is not None:
            params["producers"] = producers
            
        if params:
            json_request["params"] = params
        
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setEnableProducers(self, producers: list[dict] | list[AnalyticsMetadataProducer]):
        if isinstance(producers, list) and all(isinstance(prop, AnalyticsMetadataProducer) for prop in producers):
            producers = [self._remove_none_values(asdict(producer)) for producer in producers]
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setEnableProducers",
            "params": {
                "producers": producers
            }
        }
         
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedMetadata(self, producers: list[str] | None = None):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getSupportedMetadata",
        }
        params = {}
        if producers is not None:
            params["producers"] = producers
            
        if params:
            json_request["params"] = params
        
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
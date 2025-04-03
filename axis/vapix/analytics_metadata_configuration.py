from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase
from dataclasses import dataclass, asdict

@dataclass
class AnalyticsMetadataVideoChannel:
    channel: int | None = None
    enabled: bool | None = None

@dataclass
class AnalyticsMetadataProducer:
    name: str | None = None
    videoChannels: list[AnalyticsMetadataVideoChannel] | None = None

class AnalyticsMetadataProducerConfigurationABC(ABC):
    API_PATH = "axis-cgi/analyticsmetadataconfig.cgi"
    API_DISCOVERY_ID = "analytics-metadata-config"
    
    @abstractmethod
    def listProducers(self, producers: list[str] | None = None):
        pass
    
    @abstractmethod
    def setEnableProducers(self, producers: list[AnalyticsMetadataProducer]):
        pass
    
    @abstractmethod
    def getSupportedMetadata(self, producers: list[str] | None = None):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
class AnalyticsMetadataProducerConfigurationRequest(AnalyticsMetadataProducerConfigurationABC):
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        self.api_version = api_version
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"
    
    def listProducers(self, producers: list[str] | None = None):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "listProducers",
        }
        
        params = {}
        
        if producers is not None:
            params["producers"] = producers
            
        if params:
            json_request["params"] = params
        
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setEnableProducers(self, producers: list[AnalyticsMetadataProducer]):
        producers_dict = [asdict(producer) for producer in producers]
        
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "setEnableProducers",
            "params": {
                "producers": producers_dict
            }
        }
         
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedMetadata(self, producers: list[str] | None = None):
        json_request = {
            "apiVersion": self.api_version,
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
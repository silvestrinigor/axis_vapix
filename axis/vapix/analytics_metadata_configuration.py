from requests import Request
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

@dataclass
class AnalyticsMetadataVideoChannel:
    channel: int
    enabled: bool

@dataclass
class AnalyticsMetadataProducer:
    name: str
    videoChannels: List[AnalyticsMetadataVideoChannel | Dict]

class AnalyticsMetadataProducerConfigurationABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/analyticsmetadataconfig.cgi"
    API_DISCOVERY_ID = "analytics-metadata-config"
    
    @abstractmethod
    def listProducers(self, producers: List[str]):
        pass
    
    @abstractmethod
    def setEnableProducers(self, producers: List[Dict | AnalyticsMetadataProducer]):
        pass
    
    @abstractmethod
    def listProducers(self, producers: List[str]):
        pass
    
class AnalyticsMetadataProducerConfigurationRequest(AnalyticsMetadataProducerConfigurationABC, VapixRequestBuilderWithVersion):
    
    def listProducers(self, producers):
        return self._create_request_with_params(self.listProducers.__name__, {"producers": producers})
    
    def setEnableProducers(self, producers):
        if isinstance(producers, List) and all(isinstance(prop, AnalyticsMetadataProducer) for prop in producers):
            producers = [self._remove_none_values(asdict(producer)) for producer in producers]
        return self._create_request_with_params(self.setEnableProducers.__name__, {"producers": producers})

    def getSupportedMetadata(self, producers):
        return self._create_request_with_params(self.getSupportedMetadata.__name__, {"producers": producers})

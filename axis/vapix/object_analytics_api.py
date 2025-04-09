from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional, List, Dict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class ObjectAnalyticsDirectionType(Enum):
    LEFT_TO_RIGHT = "leftToRight"
    RIGHT_TO_LEFT = "rightToLeft"
    
class ObjectAnalyticsDeviceRotationType(Enum):
    ROTATION_0 = 0
    ROTATION_90 = 90
    ROTATION_180 = 180
    ROTATION_270 = 270

@dataclass
class ObjectAnalyticsDevice:
    id: Optional[int] = None
    type: Optional[str] = None
    rotation: Optional[int] = None # Valid values are 0, 90, 180 or 270
    isActive: Optional[bool] = None

@dataclass
class ObjectAnalyticsMetadataOverlay:
    id: Optional[int] = None
    drawOnAllResolutions: Optional[bool] = None
    resolutions: Optional[List[(int, int)]] = None # "resolutions": ["<width>x<height>", "<width>x<height>", ...]

@dataclass
class PerspectiveBar:
    height: Optional[int] = None
    points: Optional[List[List[(int, int)]]] = None # "points": [[<x>, <y>], [<x>, <y>], ...]

@dataclass
class ObjectAnalyticsPerspective:
    id: Optional[int] = None
    bars: Optional[List[PerspectiveBar]] = None

@dataclass
class ObjectAnalyticsTrigger:
    triggerType: Optional[str] = None
    vertices: Optional[List[List[(int, int)]]] = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]
    alarmDirection: Optional[str] = None # "alarmDirection": "leftToRight", "rightToLeft"
    countingDirection: Optional[str] = None # "countingDirection": "leftToRight", "rightToLeft"

@dataclass
class ScenarioFilter:
    filterType: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    time: Optional[int] = None
    distance: Optional[int] = None
    minSpeed: Optional[float] = None
    maxSpeed: Optional[float] = None
    vertices: Optional[List[List[(int, int)]]] = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]

@dataclass
class ObjectAnalyticsObjectClassificator:
    classificatorType: Optional[str] = None
    subTypes: Optional[List] = None 

@dataclass
class ObjectAnalyticsScenario:
    id: Optional[int] = None
    name: Optional[str] = None
    scenarioType: Optional[str] = None
    metadataOverlay: Optional[int] = None
    alarmRate: Optional[str] = None
    devices: Optional[List[int]] = None
    triggers: Optional[List[ObjectAnalyticsTrigger]] = None
    filters: Optional[List[ScenarioFilter]] = None
    objectClassificators: Optional[List[ObjectAnalyticsObjectClassificator]] = None
    perspectives: Optional[List[int]] = None # "perspectives": [id]
    presets: Optional[List[int]] = None # "presets": [id]

@dataclass
class ObjectAnalyticsConfiguration:
    devices: Optional[List[ObjectAnalyticsDevice]] = None
    metadataOverlay: Optional[List[ObjectAnalyticsMetadataOverlay]] = None
    perspectives: Optional[List[ObjectAnalyticsPerspective]] = None
    scenarios: Optional[List[ObjectAnalyticsScenario]] = None

class ObjectAnalyticsABC(VapixApiABC, ABC):
    API_PATH = "local/objectanalytics/control.cgi"
    
    @abstractmethod
    def getConfigurationCapabilities(self):
        pass
    
    @abstractmethod
    def setConfiguration(self, configuration: ObjectAnalyticsConfiguration | Dict):
        pass
    
    @abstractmethod
    def getConfiguration(self):
        pass
    
    @abstractmethod
    def sendAlarmEvent(self, scenario: int):
        pass
    
    @abstractmethod
    def getAccumulatedCounts(self, scenario: int):
        pass
    
    @abstractmethod
    def resetAccumulatedCounts(self, scenario: int):
        pass
    
    @abstractmethod
    def resetPassthrough(self, scenario: int):
        pass
    
    @abstractmethod
    def getOccupancy(self, scenario: int):
        pass
    
class ObjectAnalyticsRequest(ObjectAnalyticsABC, VapixRequestBuilderWithVersion):
    
    def getConfigurationCapabilities(self):
        self._create_no_params_request(self.getConfigurationCapabilities.__name__)

    def getConfiguration(self):
        self._create_no_params_request(self.getConfiguration.__name__)

    def setConfiguration(self, configuration):
        if isinstance(configuration, ObjectAnalyticsConfiguration):
            configuration = self._remove_none_values(asdict(configuration))

        return self._create_request_with_params(self.setConfiguration.__name__, configuration)
        
    def sendAlarmEvent(self, scenario):
        return self._create_request_with_params(self.sendAlarmEvent.__name__, {"scenario": scenario})

    def getAccumulatedCounts(self, scenario):
        return self._create_request_with_params(self.getAccumulatedCounts.__name__, {"scenario": scenario})

    def resetAccumulatedCounts(self, scenario):
        return self._create_request_with_params(self.resetAccumulatedCounts.__name__, {"scenario": scenario})

    def resetPassthrough(self, scenario):
        return self._create_request_with_params(self.resetPassthrough.__name__, {"scenario": scenario})

    def getOccupancy(self, scenario):
        return self._create_request_with_params(self.getOccupancy.__name__, {"scenario": scenario})
        
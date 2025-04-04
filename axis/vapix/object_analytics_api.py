from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from requests.auth import AuthBase
from enum import Enum
from .requests import VapixApiRequest
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
    id: int | None = None
    type: str | None = None
    rotation: int | None = None # Valid values are 0, 90, 180 or 270
    isActive: bool | None = None

@dataclass
class ObjectAnalyticsMetadataOverlay:
    id: int | None = None
    drawOnAllResolutions: bool | None = None
    resolutions: list[(int, int)] | None = None # "resolutions": ["<width>x<height>", "<width>x<height>", ...]

@dataclass
class PerspectiveBar:
    height: int | None = None
    points: list[list[(int, int)]] | None = None # "points": [[<x>, <y>], [<x>, <y>], ...]

@dataclass
class ObjectAnalyticsPerspective:
    id: int | None = None
    bars: list[PerspectiveBar] | None = None

@dataclass
class ObjectAnalyticsTrigger:
    triggerType: str | None = None
    vertices: list[list[(int, int)]] | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]
    alarmDirection: str | None = None # "alarmDirection": "leftToRight", "rightToLeft"
    countingDirection: str | None = None # "countingDirection": "leftToRight", "rightToLeft"

@dataclass
class ScenarioFilter:
    filterType: str | None = None
    width: int | None = None
    height: int | None = None
    time: int | None = None
    distance: int | None = None
    minSpeed: float | None = None
    maxSpeed: float | None = None
    vertices: list[list[(int, int)]] | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]

@dataclass
class ObjectAnalyticsObjectClassificator:
    classificatorType: str | None = None
    subTypes: list | None = None 

@dataclass
class ObjectAnalyticsScenario:
    id: int | None = None
    name: str | None = None
    scenarioType: str | None = None
    metadataOverlay: int | None = None
    alarmRate: str | None = None
    devices: list[int] | None = None
    triggers: list[ObjectAnalyticsTrigger] | None = None
    filters: list[ScenarioFilter] | None = None
    objectClassificators: list[ObjectAnalyticsObjectClassificator] | None = None
    perspectives: list[int] | None = None # "perspectives": [id]
    presets: list[int] | None = None # "presets": [id]

@dataclass
class ObjectAnalyticsConfiguration:
    devices: list[ObjectAnalyticsDevice] | None = None
    metadataOverlay: list[ObjectAnalyticsMetadataOverlay] | None = None
    perspectives: list[ObjectAnalyticsPerspective] | None = None
    scenarios: list[ObjectAnalyticsScenario] | None = None

class ObjectAnalyticsABC(VapixApiABC, ABC):
    API_PATH = "local/objectanalytics/control.cgi"
    
    @abstractmethod
    def getConfigurationCapabilities(self):
        pass
    
    @abstractmethod
    def setConfiguration(self):
        pass
    
    @abstractmethod
    def getConfiguration(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
    @abstractmethod
    def sendAlarmEvent(self):
        pass
    
    @abstractmethod
    def getAccumulatedCounts(self):
        pass
    
    @abstractmethod
    def resetAccumulatedCounts(self):
        pass
    
    @abstractmethod
    def resetPassthrough(self):
        pass
    
    @abstractmethod
    def getOccupancy(self):
        pass
    
class ObjectAnalyticsRequest(ObjectAnalyticsABC, VapixApiRequest):
    
    def getConfigurationCapabilities(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getConfigurationCapabilities",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getConfiguration(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getConfiguration",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setConfiguration(self, configuration: ObjectAnalyticsConfiguration):
        if isinstance(configuration, ObjectAnalyticsConfiguration):
            configuration = self._remove_none_values(asdict(configuration))

        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setConfiguration",
            "params": configuration
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def sendAlarmEvent(self, scenario: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "sendAlarmEvent",
            "params": {
                "scenario": scenario
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getAccumulatedCounts(self, scenario: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getAccumulatedCounts",
            "params": {
                "scenario": scenario
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def resetAccumulatedCounts(self, scenario: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "resetAccumulatedCounts",
            "params": {
                "scenario": scenario
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def resetPassthrough(self, scenario: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "resetPassthrough",
            "params": {
                "scenario": scenario
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getOccupancy(self, scenario: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getOccupancy",
            "params": {
                "scenario": scenario
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

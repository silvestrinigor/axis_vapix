"""
https://developer.axis.com/vapix/applications/axis-object-analytics-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from .connection import ApiVersion
from .abc import VapixApi
from .requests import AxisSession

PATH = "local/objectanalytics/control.cgi"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}

class MethodType(Enum):
    GET_CONFIGURATION_CAPABILITIES = "getConfigurationCapabilities"
    SET_CONFIGURATION = "setConfiguration"
    GET_CONFIGURATION = "get_configuration"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    SEND_ALARM = "sendAlarm"
    GET_ACCUMULATED_COUNTS = "getAccumulatedCounts"
    RESET_ACCUMULATED_COUNTS = "resetAccumulatedCounts"
    RESET_PASSTHROUGH = "resetPassthrough"
    GET_OCCUPANCY = "getOccupancy"


@dataclass
class ObjectAnalyticsDevice:
    id: int | None = None
    deviceYype: str | None = None
    rotation: str | None = None
    isActive: bool | None = None


@dataclass
class ObjectAnalyticsMetadataOverlay:
    id: int | None = None
    drawOnAllResolutions: bool | None = None
    resolutions: list[int] | None = None # "resolutions": ["<width>x<height>", "<width>x<height>", ...]


@dataclass
class PerspectiveBar:
    height: int | None = None
    points: list | None = None # "points": [[<x>, <y>], [<x>, <y>], ...]


@dataclass
class ObjectAnalyticsPerspective:
    id: int | None = None
    bars: list[PerspectiveBar] | None = None


@dataclass
class ObjectAnalyticsTrigger:
    triggerType: str | None = None
    vertices: list | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]
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
    vertices: list | None = None # "vertices": [[<x>, <y>], [<x>, <y>], ...]


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


class ObjectAnalyticsApi(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)
    
    def get_configuration_capabilities(self):
        body = self._create_body(MethodType.GET_CONFIGURATION_CAPABILITIES)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_configuration(self):
        body = self._create_body(MethodType.GET_CONFIGURATION)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_configuration(self, configuration: ObjectAnalyticsConfiguration):
        params = asdict(configuration)        
        body = self._create_body(MethodType.SET_CONFIGURATION, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
     
    def send_alarm(self, scenario: int):
        params = {"scenario": scenario}
        body = self._create_body(MethodType.SEND_ALARM, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_accumulated_count(self, scenario: int):
        params = {"scenario": scenario}
        body = self._create_body(MethodType.GET_ACCUMULATED_COUNTS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def reset_accumulated_count(self, scenario: int):
        params = {"scenario": scenario}
        body = self._create_body(MethodType.RESET_ACCUMULATED_COUNTS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def reset_passthroungh(self, scenario: int):
        params = {"scenario": scenario}
        body = self._create_body(MethodType.RESET_PASSTHROUGH, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_occupancy(self, scenario: int):
        params = {"scenario": scenario}
        body = self._create_body(MethodType.GET_OCCUPANCY, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from .requests import VapixApiRequest
from .api import VapixApiABC

@dataclass
class LoiteringGuardCamera:
    active: bool | None = None
    rotation: str | None = None
    overlayResolution: str | None = None

@dataclass
class ProfileFilter:
    filterType: str | None = None
    data: list | None = None
    active: bool | None = None

@dataclass
class LoiteringGuardTrigger:
    triggerType: str | None = None
    data: list | None = None
    active: bool | None = None

@dataclass
class LoiteringGuardPerspective:
    triggerType: str | None = None
    data: list | None = None
    height: int | None = None

@dataclass
class LoiteringGuardProfile:
    name: str | None = None
    uid: int | None = None
    camera: int | None = None
    alarmOverlayEnabled: bool | None = None
    filters: list[ProfileFilter] | None = None
    triggers: list[LoiteringGuardTrigger] | None = None
    presets: list | None = None
    perspectives: list[LoiteringGuardPerspective] | None = None

@dataclass
class LoiteringGuardConfiguration:
    cameras: list[LoiteringGuardCamera] | None = None
    profiles: list[LoiteringGuardProfile] | None = None

class LoiteringGuardABC(VapixApiABC, ABC):
    API_PATH = "local/loiteringguard/control.cgi"
    
    @abstractmethod
    def getConfiguration(self):
        pass

    @abstractmethod
    def setConfiguration(self, configuration: LoiteringGuardConfiguration | dict):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
    @abstractmethod
    def sendAlarmEvent(self, scenario: int):
        pass
    
    @abstractmethod
    def getConfigurationCapabilities(self):
        pass

class LoiteringGuardRequest(LoiteringGuardABC, VapixApiRequest):
    
    def getConfiguration(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getConfiguration",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setConfiguration(self, configuration: LoiteringGuardConfiguration | dict):
        if isinstance(configuration, LoiteringGuardConfiguration):
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

    def getConfigurationCapabilities(self):
        json_request = {
            "context": self.context,
            "method": "getConfigurationCapabilities",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

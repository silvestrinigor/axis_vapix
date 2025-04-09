from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional, List, Dict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

@dataclass
class LoiteringGuardCamera:
    active: Optional[bool] = None
    rotation: Optional[str] = None
    overlayResolution: Optional[str] = None

@dataclass
class ProfileFilter:
    filterType: Optional[str] = None
    data: Optional[List] = None
    active: Optional[bool] = None

@dataclass
class LoiteringGuardTrigger:
    triggerType: Optional[str] = None
    data: Optional[List] = None
    active: Optional[bool] = None

@dataclass
class LoiteringGuardPerspective:
    triggerType: Optional[str] = None
    data: Optional[List] = None
    height: Optional[int] = None

@dataclass
class LoiteringGuardProfile:
    name: Optional[str] = None
    uid: Optional[int] = None
    camera: Optional[int] = None
    alarmOverlayEnabled: Optional[bool] = None
    filters: Optional[List[ProfileFilter]] = None
    triggers: Optional[List[LoiteringGuardTrigger]] = None
    presets: Optional[List] = None
    perspectives: Optional[List[LoiteringGuardPerspective]] = None

@dataclass
class LoiteringGuardConfiguration:
    cameras: Optional[List[LoiteringGuardCamera]] = None
    profiles: Optional[List[LoiteringGuardProfile]] = None

class LoiteringGuardABC(VapixApiABC, ABC):
    API_PATH = "local/loiteringguard/control.cgi"
    
    @abstractmethod
    def getConfiguration(self):
        pass

    @abstractmethod
    def setConfiguration(self, configuration: LoiteringGuardConfiguration | Dict):
        pass
    
    @abstractmethod
    def sendAlarmEvent(self, scenario: int):
        pass
    
    @abstractmethod
    def getConfigurationCapabilities(self):
        pass

class LoiteringGuardRequest(LoiteringGuardABC, VapixRequestBuilderWithVersion):
    
    def getConfiguration(self):
        return self._create_no_params_request(self.getConfiguration.__name__)

    def setConfiguration(self, configuration):
        if isinstance(configuration, LoiteringGuardConfiguration):
            configuration = self._remove_none_values(asdict(configuration))

        return self._create_request_with_params(self.setConfiguration.__name__, configuration)

    def sendAlarmEvent(self, scenario):
        return self._create_request_with_params(self.sendAlarmEvent.__name__, {"scenario": scenario})

    def getConfigurationCapabilities(self):
        return self._create_no_params_request(self.getConfigurationCapabilities.__name__)

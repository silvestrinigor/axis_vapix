"""
https://developer.axis.com/vapix/applications/loitering-guard
"""
from enum import Enum
from dataclasses import dataclass, asdict
from ..connection import ApiVersion
from ..abc import VapixApi
from ..requests import AxisSession

PATH = "local/loiteringguard/control.cgi"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}


class MethodType(Enum):
    GET_CONFIGURATION = "getConfiguration"
    SET_CONFIGURATION = "setConfiguration"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    SEND_ALARM_EVENT = "sendAlarmEvent"
    GET_CONFIGURATION_CAPABILITIES = "getConfigurationCapabilities"


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



class LoiteringGuard(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)
    
    def get_configuration(self):
        body = self._create_body(MethodType.GET_CONFIGURATION)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_configuration(self, configuration: LoiteringGuardConfiguration):
        params = asdict(configuration)
        body = self._create_body(MethodType.SET_CONFIGURATION, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def send_alarm_event(self, profile: int):
        params = {"profile": profile}
        body = self._create_body(MethodType.SEND_ALARM_EVENT, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_configuration_capabilities(self):
        body = self._create_body(MethodType.GET_CONFIGURATION_CAPABILITIES)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
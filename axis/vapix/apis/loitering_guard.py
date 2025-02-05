"""
https://developer.axis.com/vapix/applications/loitering-guard
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..api import IVapixApiClass, ApiVersion
from ..requests import VapixRequest, AxisSession
from .. import utils

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
    perspectives: list[LoiteringGuardPerspective] | None


@dataclass
class LoiteringGuardConfiguration:
    cameras: list[LoiteringGuardCamera] | None = None
    profiles: list[LoiteringGuardProfile] | None = None



class LoiteringGuard(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)
    
    def get_configuration(self):
        body = self._create_body(MethodType.GET_CONFIGURATION)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def set_configuration(self, configuration: LoiteringGuardConfiguration):
        params = asdict(configuration)
        body = self._create_body(MethodType.SET_CONFIGURATION, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def send_alarm_event(self, profile: int):
        params = {"profile": profile}
        body = self._create_body(MethodType.SEND_ALARM_EVENT, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def get_configuration_capabilities(self):
        body = self._create_body(MethodType.GET_CONFIGURATION_CAPABILITIES)
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
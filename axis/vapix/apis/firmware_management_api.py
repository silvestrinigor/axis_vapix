"""
https://developer.axis.com/vapix/network-video/firmware-management-api
"""
from enum import Enum
import json
from .connection import ApiVersion, FirmwareVersion
from .abc import VapixApi
from .requests import VapixRequest, AxisSession

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(7, 40, 0)
DISCOVERY_API_ID = "fwmgr"
PATH = "axis-cgi/firmwaremanagement.cgi"
REQUEST_METHOD = "POST"


PROPERTIES = [
    "Properties.FirmwareManagement.Version=1.3"
]


BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}


class MethodType(Enum):
    STATUS = "status"
    UPGRADE = "upgrade"
    COMMIT = "commit"
    ROLLBACK = "rollback"
    PURGE = "purge"
    FACTORY_DEFAULT = "factoryDefault"
    STOP_AUTO = "stopAuto"
    REBOOT = "reboot"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


class FactoryDefaultModeType(Enum):
    SOFT = "soft"
    HARD = "hard"
    NONE = None


class AutoCommitType(Enum):
    NEVER = "never"
    BOOT = "boot"
    STARTED = "started"
    DEFAULT = "default"
    NONE = None


class FirmwareManagementApi(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)

    def status(self):
        body = self._create_body(MethodType.STATUS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def upgrade(self, 
            file_path: str, 
            factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE,
            auto_commit: AutoCommitType = AutoCommitType.NONE
        ):
        
        params = {}
        if factory_default != FactoryDefaultModeType.NONE:
            params["factoryDefaultMode"] = factory_default.value
        if auto_commit != AutoCommitType.NONE:
            params["autoCommit"] = auto_commit.value
        if params == {}:
            params = None
        
        body = self._create_body(MethodType.UPGRADE, params)
        json_data = json.dumps(body).encode("utf-8")
        
        with open(file_path, 'rb') as firmware_file: # Using with open in Python is a best practice for handling files because it ensures that the file is properly closed
            firmware = firmware_file.read() 
        
        request = VapixRequest(
            method=REQUEST_METHOD,
            url=self._base_url + PATH,
            files=((None, json_data),(None,firmware))
        )
        
        response = self._send_request(request)
        return response

    def commit(self):
        body = self._create_body(MethodType.COMMIT)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def rollback(self):
        body = self._create_body(MethodType.ROLLBACK)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def purge(self):
        body = self._create_body(MethodType.PURGE)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def factory_default(self, factory_default: FactoryDefaultModeType = FactoryDefaultModeType.NONE):
        params = {}
        if factory_default != FactoryDefaultModeType.NONE:
            params["factoryDefaultMode"] = factory_default.value
        if params == {}:
            params = None
        
        body = self._create_body(MethodType.FACTORY_DEFAULT, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def stop_auto(self):
        body = self._create_body(MethodType.STOP_AUTO)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def reboot(self):
        body = self._create_body(MethodType.REBOOT)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
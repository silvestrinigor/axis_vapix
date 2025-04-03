"""
https://developer.axis.com/vapix/network-video/capture-mode/
"""
from enum import Enum
from .connection import ApiVersion, FirmwareVersion
from .abc import VapixApi
from .requests import AxisSession

LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 50, 0)
PATH = "axis-cgi/capturemode.cgi"
REQUEST_METHOD = "POST"

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "channel": None,
    "captureModeId": None
}

class MethodType(Enum):
    GET_CAPTURE_MODE = "getCaptureModes"
    SET_CAPTURE_MODE = "setCaptureMode"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"


class CaptureMode(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion, path):
        super().__init__(session, api_version, path=PATH, body=BODY)

    def get_capture_mode(self):
        body = self._create_body(MethodType.GET_CAPTURE_MODE)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_capture_mode(self, channel: int, capture_mode_id: int):
        body = self._create_body(MethodType.GET_CAPTURE_MODE)
        body["channel"] = channel
        body["captureModeId"] = capture_mode_id
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
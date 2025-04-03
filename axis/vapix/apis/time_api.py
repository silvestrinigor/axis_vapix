"""
https://developer.axis.com/vapix/network-video/time-api
"""

from datetime import datetime
from enum import Enum
from .connection import ApiVersion, FirmwareVersion
from .abc import VapixApi
from .requests import AxisSession
from . import utils

PATH = "axis-cgi/time.cgi"
REQUEST_METHOD = "POST"
LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(9, 30, 0)

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}

class MethodType(Enum):
    GET_DATE_TIME_INFO = "getDateTimeInfo"
    GET_ALL = "getAll"
    SET_DATE_TIME = "setDateTime"
    SET_TIME_ZONE = "setTimeZone"
    SET_POSIX_TIME_ZONE = "setPosixTimeZone"
    RESET_TIME_ZONE = "resetTimeZone"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    

class TimeApi(VapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH, body=BODY)
    
    def get_date_time_info(self):
        body = self._create_body(MethodType.GET_DATE_TIME_INFO)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_all(self):
        body = self._create_body(MethodType.GET_ALL)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def set_date_time(self, date_time: datetime):
        serialized_date_time = utils.serialize_datetime(date_time)
        params = {"dateTime": serialized_date_time}

        body = self._create_body(MethodType.SET_DATE_TIME, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def set_time_zone(self, timezone: str):
        params = {"timezone": timezone}
        body = self._create_body(MethodType.SET_DATE_TIME, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def set_posix_time_zone(self, posix_timezone: str, enable_dst: bool):
        params = {
            "posixTimezone" : posix_timezone,
            "enableDst" : enable_dst
        }
        body = self._create_body(MethodType.SET_DATE_TIME, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
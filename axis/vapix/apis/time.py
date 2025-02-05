"""
https://developer.axis.com/vapix/network-video/time-api
"""

from enum import Enum
from datetime import datetime
from dataclasses import dataclass, asdict
from ..api import IVapixApiClass, ApiVersion, FirmwareVersion
from ..requests import VapixRequest, AxisSession
from .. import utils

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
    

class TimeApi(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)
    
    def get_date_time_info(self):
        body = self._create_body(MethodType.GET_DATE_TIME_INFO)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def get_all(self):
        body = self._create_body(MethodType.GET_ALL)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def set_date_time(self, date_time: datetime):
        serialized_date_time = utils.serialize_datetime(date_time)
        params = {"dateTime": serialized_date_time}

        body = self._create_body(MethodType.SET_DATE_TIME, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def set_time_zone(self, timezone: str):
        params = {"timezone": timezone}
        body = self._create_body(MethodType.SET_DATE_TIME, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def set_posix_time_zone(self, posix_timezone: str, enable_dst: bool):
        params = {
            "posixTimezone" : posix_timezone,
            "enableDst" : enable_dst
        }
        body = self._create_body(MethodType.SET_DATE_TIME, params)
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
"""
https://developer.axis.com/vapix/network-video/time-api
"""

from datetime import datetime
from ..request import AxisRequest
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType, ParamType
from ..params import ApiVersion, FirmwareVersion
from ..utils import serialize_datetime

TIME_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(9, 30, 0)
TIME_API_DISCOVERY_API_ID = "time-service"

class RequestTimeApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_TIME
    
    def get_date_time_info(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_DATE_TIME_INFO.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def get_all(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_ALL.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_date_time(self, date_time: datetime):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_DATE_TIME.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.DATE_TIME.value: serialize_datetime(date_time)}
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_time_zone(self, timezone: str):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_TIME_ZONE.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.TIME_ZONE.value: timezone}
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def set_posix_time_zone(self, posix_timezone: str, enable_dst: bool):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_POSIX_TIME_ZONE.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.POSIX_TIME_ZONE.value: posix_timezone}
        request_body[RequestParamType.PARAMS.value][ParamType.ENABLE_DST.value] = enable_dst
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def reset_time_zone(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.RESET_TIME_ZONE.value
        return AxisRequest("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)
    
    def get_suported_versions(self):
        return super()._get_supported_versions()

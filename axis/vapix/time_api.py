from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase
from datetime import datetime, timezone

class TimeApiABC(ABC):
    API_PATH = "axis-cgi/time.cgi"
    API_DISCOVERY_ID = "time-service"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "9.30"

    @abstractmethod
    def getDateTimeInfo(self):
        pass
    
    @abstractmethod
    def getAll(self):
        pass
    
    @abstractmethod
    def setDateTime(self, date_time: str):
        pass
    
    @abstractmethod
    def setTimeZone(self):
        pass
    
    @abstractmethod
    def setPosixTimeZone(self):
        pass
    
    @abstractmethod
    def resetTimeZone(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass

class TimeApiRequest(TimeApiABC):
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        self.api_version = api_version
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

    def getDateTimeInfo(self):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getDateTimeInfo",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAll(self):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getAll",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setDateTime(self, date_time: str | datetime):
        if isinstance(date_time, datetime):
            date_time = self._serialize_datetime(date_time)
        
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "setDateTime",
            "params": {
                "dateTime": date_time
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setTimeZone(self, time_zone: str):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "setTimeZone",
            "params": {
                "timeZone": time_zone
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setPosixTimeZone(self, posix_time_zone: str, enable_dst: bool):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "setPosixTimeZone",
            "params": {
                "posixTimeZone": posix_time_zone,
                "enableDst": enable_dst
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def resetTimeZone(self):
        json_request = {
            "context": self.context,
            "method": "resetTimeZone",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def _serialize_datetime(self, date_time: datetime) -> str:
        if not self._is_timezone_aware(date_time=date_time): 
            raise ValueError("The datetime object must be timezone-aware")
        date_time_utc = date_time.astimezone(timezone.utc)
        serialized_date_time = date_time_utc.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        return serialized_date_time

    def _is_timezone_aware(self, date_time: datetime) -> bool:
        return date_time.tzinfo is not None and date_time.tzinfo.utcoffset(date_time) is not None

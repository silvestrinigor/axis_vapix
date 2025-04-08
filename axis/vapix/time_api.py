from abc import ABC, abstractmethod
from requests import Request
from datetime import datetime
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class TimeApiABC(VapixApiABC, ABC):
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
    def setDateTime(self, date_time: str | datetime):
        pass
    
    @abstractmethod
    def setTimeZone(self, time_zone: str):
        pass
    
    @abstractmethod
    def setPosixTimeZone(self, posix_time_zone: str, enable_dst: bool):
        pass
    
    @abstractmethod
    def resetTimeZone(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass

class TimeApiRequest(TimeApiABC, VapixRequestBuilderWithVersion):

    def getDateTimeInfo(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getDateTimeInfo",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAll(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getAll",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setDateTime(self, date_time: str | datetime):
        if isinstance(date_time, datetime):
            date_time = self._serialize_datetime(date_time)
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setDateTime",
            "params": {
                "dateTime": date_time
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setTimeZone(self, time_zone: str):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setTimeZone",
            "params": {
                "timeZone": time_zone
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def setPosixTimeZone(self, posix_time_zone: str, enable_dst: bool):
        json_request = {
            "apiVersion": self.apiVersion,
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
        return super().getSupportedVersions()
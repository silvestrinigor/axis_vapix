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
    
class TimeApiRequest(TimeApiABC, VapixRequestBuilderWithVersion):

    def getDateTimeInfo(self):
        return self._create_no_params_request(self.getDateTimeInfo.__name__)
    
    def getAll(self):
        return self._create_no_params_request(self.getAll.__name__)
    
    def setDateTime(self, date_time: str | datetime):
        if isinstance(date_time, datetime):
            date_time = self._serialize_datetime(date_time)
        return self._create_request_with_params(self.setDateTime.__name__, {"dateTime": date_time})
    
    def setTimeZone(self, time_zone: str):
        return self._create_request_with_params(self.setTimeZone.__name__, {"timeZone": time_zone})
    
    def setPosixTimeZone(self, posix_time_zone: str, enable_dst: bool):
        params = {
            "posixTimeZone": posix_time_zone,
            "enableDst": enable_dst
        }
        return self._create_request_with_params(self.setPosixTimeZone.__name__, params)
    
    def resetTimeZone(self):
        return self._create_no_params_request(self.resetTimeZone.__name__)

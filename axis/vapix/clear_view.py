from abc import ABC, abstractmethod
from requests import Request
from typing import Optional
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class ClearViewABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/clearviewcontrol.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "7.10"

    @abstractmethod
    def getServiceInfo(self):
        pass
    
    @abstractmethod
    def getStatus(self, id: int):
        pass
    
    @abstractmethod
    def start(self, id: int, duration: Optional[int] = None):
        pass
    
    @abstractmethod
    def stop(self, id: int):
        pass
        
class ClearViewRequest(ClearViewABC, VapixRequestBuilderWithVersion):

    def getServiceInfo(self):
        return self._create_request_with_params(self.getServiceInfo.__name__, {})
    
    def getStatus(self, id):
        return self._create_request_with_params(self.getStatus.__name__, {"id": id})

    def start(self, id, duration = None):
        params = {"id": id}
        if duration is not None:
            params["duration"] = duration
        return self._create_request_with_params(self.start.__name__, params)
        
    def stop(self, id):
        return self._create_request_with_params(self.stop.__name__, {"id": id})

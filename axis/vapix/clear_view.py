from abc import ABC, abstractmethod
from requests import Request
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class ClearViewABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/clearviewcontrol.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "7.10"

    @abstractmethod
    def getSupportedVersions(self):
        pass
    
    @abstractmethod
    def getServiceInfo(self):
        pass
    
    @abstractmethod
    def getStatus(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
        
class ClearViewRequest(ClearViewABC, VapixRequestBuilderWithVersion):

    def getServiceInfo(self):
        json_request = {
            "context": self.context,
            "method": "getServiceInfo",
            "params": {
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getStatus(self, id: int):
        json_request = {
            "context": self.context,
            "method": "getStatus",
            "params": {
                "id": id
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def start(self, id: int, duration: int | None = None):
        json_request = {
            "context": self.context,
            "method": "start",
            "params": {
                "id": id
            }
        }
        if duration is not None:
            json_request["params"]["duration"] = duration
        
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def stop(self, id: int):
        json_request = {
            "context": self.context,
            "method": "stop",
            "params": {
                "id": id
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        return super().getSupportedVersions()
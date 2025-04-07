from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase
from .requests import VapixApiRequestWithVersion
from .api import VapixApiABC

class CustomHTTPheaderAPIABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/customhttpheader.cgi"
    API_DISCOVERY_ID = "customhttpheader"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "9.80"

    @abstractmethod
    def list(self):
        pass
    
    @abstractmethod
    def set(self, CustomHeaderName, CustomHeaderValue):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
class CustomHTTPheaderAPIRequest(VapixApiABC, VapixApiRequestWithVersion):
    
    def list(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def set(self, CustomHeaderName, CustomHeaderValue):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "set",
            "params": {
                CustomHeaderName: CustomHeaderValue
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def remove(self, CustomHeaderName, CustomHeaderValue):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "remove",
            "params": {
                CustomHeaderName: CustomHeaderValue
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        return super().getSupportedVersions()
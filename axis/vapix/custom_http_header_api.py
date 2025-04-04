from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase
from .requests import VapixApiRequest
from .api import VapixApiABC

class CustomHTTPheaderAPIABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/customhttpheader.cgi"
    API_DISCOVERY_ID = "customhttpheader"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "9.80"

    @abstractmethod
    def list(self):
        pass
    
    @abstractmethod
    def set(self):
        pass
    
    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
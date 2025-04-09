from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase
from .requests import VapixRequestBuilderWithVersion
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
    
class CustomHTTPheaderAPIRequest(VapixApiABC, VapixRequestBuilderWithVersion):
    
    def list(self):
        return self._create_no_params_request(self.list.__name__)
        
    def set(self, CustomHeaderName, CustomHeaderValue):
        return self._create_request_with_params(self.set.__name__, {CustomHeaderName: CustomHeaderValue})
    
    def remove(self, CustomHeaderName, CustomHeaderValue):
        return self._create_request_with_params(self.remove.__name__, {CustomHeaderName: CustomHeaderValue})

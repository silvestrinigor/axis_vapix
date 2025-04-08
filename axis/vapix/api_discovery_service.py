from abc import ABC, abstractmethod
from requests import Request
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class ApiDiscoveryServiceABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/apidiscovery.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"
    
    @abstractmethod
    def getApiList(self, id = None, version = None):
        pass
    
    def getSupportedVersions(self):
        pass
    
class ApiDiscoveryServiceRequest(ApiDiscoveryServiceABC, VapixRequestBuilderWithVersion):
    
    def getApiList(self, id=None, version=None):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getApiList",
        }
        params = {}
        if id is not None:
            params["id"] = id
        if version is not None:
            params["version"] = version
        if params:
            json_request["params"] = params
        
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        return super().getSupportedVersions()
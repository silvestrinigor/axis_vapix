from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase

class ApiDiscoveryServiceABC(ABC):
    API_PATH = "axis-cgi/apidiscovery.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"
    
    @abstractmethod
    def getApiList(self, id = None, version = None):
        pass
    
    def getSupportedVersions(self):
        pass
    
class ApiDiscoveryServiceRequest(ApiDiscoveryServiceABC):
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        self.api_version = api_version
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

    def getApiList(self, id=None, version=None):
        json_request = {
            "apiVersion": self.api_version,
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
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
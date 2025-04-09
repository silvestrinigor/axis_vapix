from abc import ABC, abstractmethod
from requests import Request
from typing import Optional
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class ApiDiscoveryServiceABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/apidiscovery.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"
    
    @abstractmethod
    def getApiList(self, id: Optional[str] = None, version: Optional[str] = None):
        pass
    
class ApiDiscoveryServiceRequest(ApiDiscoveryServiceABC, VapixRequestBuilderWithVersion):
    
    def getApiList(self, id=None, version=None):
        params = {}
        if id is not None:
            params["id"] = id
        if version is not None:
            params["version"] = version
        if params:
            return self._create_request_with_params(self.getApiList.__name__, params)
        else:
            return self._create_no_params_request(self.getApiList.__name__)
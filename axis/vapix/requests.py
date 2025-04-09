from requests import Request
from typing import Dict
from .api import VapixApiABC, VapixApiWithVersionABC

class VapixRequestBuilder(VapixApiABC):
    
    def __init__(self, host, port, auth = None, secure: bool = False):
        protocol = "https" if secure else "http"        
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

class VapixRequestBuilderWithVersion(VapixApiWithVersionABC, VapixRequestBuilder):
    def __init__(self, host, port, auth = None, secure = False, api_version = "1.0", context = None):
        self.context = context
        self.apiVersion = api_version

        self._BASE_JSON_REQUEST = {
            "apiVersion": str(self.apiVersion),
        }
        if context is not None:
            self._BASE_JSON_REQUEST["context"] = str(context)
        
        super().__init__(host, port, auth, secure)

    def getSupportedVersions(self):
        json_request = {
            "method": str(self.getSupportedVersions.__name__)
        }
        if self.context is not None:
            json_request["context"] = str(self.context)

        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def _create_no_params_request(self, method: str):
        json_request = self._BASE_JSON_REQUEST
        json_request["method"] = str(method)
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def _create_request_with_params(self, method: str, params: Dict):
        json_request = self._BASE_JSON_REQUEST
        json_request["method"] = str(method)
        json_request["params"] = params
        return Request("POST", self.url, json=json_request, auth=self.auth)

from requests.auth import AuthBase
from requests import Request
from packaging.version import Version

class VapixApiRequest:
    API_PATH = "axis-cgi"
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False):
        protocol = "https" if secure else "http"        
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

class VapixApiRequestWithVersion(VapixApiRequest):
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str | Version = "1.0", context: str = ""):
        self.context = context

        if isinstance(api_version, Version):
            api_version = str(api_version)
        self.apiVersion = api_version

        super().__init__(host, port, auth, secure)

    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions"
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
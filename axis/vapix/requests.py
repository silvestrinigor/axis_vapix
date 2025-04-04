from requests.auth import AuthBase
from packaging.version import Version

class VapixApiRequest:
    API_PATH = ""
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str | Version = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        
        if isinstance(api_version, Version):
            api_version = str(api_version)
        self.apiVersion = api_version
        
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

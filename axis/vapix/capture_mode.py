from abc import ABC, abstractmethod
from requests import Request
from requests.auth import AuthBase

class CaptureModeABC(ABC):
    API_PATH = "axis-cgi/capturemode.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"
    
    @abstractmethod
    def getCaptureModes(self):
        pass
    
    @abstractmethod
    def setCaptureMode(self, channel: int, captureModeId: int):
        pass

class CaptureModeRequest(CaptureModeABC):

    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        self.api_version = api_version
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

    def getCaptureModes(self):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getCaptureModes",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setCaptureMode(self, channel: int, captureModeId: int):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "setCaptureModes",
            "channel": channel,
            "captureModeId": captureModeId,
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

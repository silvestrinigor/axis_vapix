from abc import ABC, abstractmethod
from requests import Request
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class CaptureModeABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/capturemode.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.50"
    
    @abstractmethod
    def getCaptureModes(self):
        pass
    
    @abstractmethod
    def setCaptureMode(self, channel: int, captureModeId: int):
        pass

class CaptureModeRequest(CaptureModeABC, VapixRequestBuilderWithVersion):

    def getCaptureModes(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getCaptureModes"
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setCaptureMode(self, channel: int, captureModeId: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setCaptureModes",
            "channel": channel,
            "captureModeId": captureModeId
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        return super().getSupportedVersions()
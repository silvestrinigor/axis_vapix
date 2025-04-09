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
        return self._create_no_params_request(self.getCaptureModes.__name__)
    
    def setCaptureMode(self, channel, captureModeId):
        json_request = self._BASE_JSON_REQUEST
        json_request["method"] = str(self.setCaptureMode.__name__)
        json_request["channel"] = channel
        json_request["captureModeId"] = captureModeId
        return Request("POST", self.url, json=json_request, auth=self.auth)

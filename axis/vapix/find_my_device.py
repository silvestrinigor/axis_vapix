from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional
import json
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class FindMyDeviceABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/findmydevice.cgi"
    API_DISCOVERY_ID = "findmydevice"

    @abstractmethod
    def find(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class FindMyDeviceRequest(FindMyDeviceABC, VapixRequestBuilderWithVersion):
    
    def find(self, duration: Optional[int]):
        if duration is not None:
            return self._create_request_with_params(self.find.__name__, {"duration": duration})
        return self._create_no_params_request(self.find.__name__)
    
    def stop(self):
        return self._create_no_params_request(self.stop.__name__)
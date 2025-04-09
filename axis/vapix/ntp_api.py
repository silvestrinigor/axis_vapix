from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional, List, Dict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

@dataclass
class NTPClientConfiguration:
    enable: Optional[bool] = None
    NTSEnabled: Optional[bool] = None
    NTSKEServerCACerts: Optional[List[str]] = None
    serversSource = Optional[str] = None
    staticServers : Optional[List[str]] = None
    staticNTSKEServers: Optional[List[str]] = None

class NtpApiABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/ntp.cgi"
    API_DISCOVERY_ID = "ntp"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "9.10"

    @abstractmethod
    def getNTPInfo(self):
        pass
    
    @abstractmethod
    def setNTPClientConfiguration(self, configuration: Dict | NTPClientConfiguration):
        pass

class NtpApiRequest(VapixApiABC, VapixRequestBuilderWithVersion):
    
    def getNTPInfo(self):
        return self._create_no_params_request(self.getNTPInfo.__name__)
    
    def setNTPClientConfiguration(self, configuration):
        if isinstance(configuration, NTPClientConfiguration):
            configuration = self._remove_none_values(asdict(configuration))
        return self._create_request_with_params(self.setNTPClientConfiguration.__name__, configuration)
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from requests import Request
from enum import Enum
from typing import Optional
import json
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class FactoryDefaultModeType(Enum):
    DEFAULT = "none"
    SOFT = "soft"
    HARD = "hard"

class AutoCommitType(Enum):
    NEVER = "never"
    BOOT = "boot"
    STARTED = "started"
    DEFAULT = "default"

class AutoRollbackType(Enum):
    NEVER = "never"
    DEFAULT = "default"

class FirmwareManagementApiABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/firmwaremanagement.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "7.40"
    API_DISCOVERY_ID = "fwmgr"

    @abstractmethod
    def status(self):
        pass
    
    @abstractmethod
    def upgrade(self, firmware_bytes_or_path: str | bytes, factoryDefaultMode: Optional[str | FactoryDefaultModeType] = None, autoCommit: Optional[str | AutoCommitType] = None, autoRollback: Optional[str | AutoRollbackType] = None):
        pass
    
    @abstractmethod
    def commit(self):
        pass
    
    @abstractmethod
    def roolback(self):
        pass
    
    @abstractmethod
    def purge(self):
        pass
    
    @abstractmethod
    def factoryDefault(self, mode: str | FactoryDefaultModeType):
        pass
    
    @abstractmethod
    def stopAuto(self):
        pass
    
    @abstractmethod
    def reboot(self):
        pass
    
class FirmwareManagementApiRequest(FirmwareManagementApiABC, VapixRequestBuilderWithVersion):
    
    def status(self):
        return self._create_no_params_request(self.status.__name__)
    
    def upgrade(self, firmware_bytes_or_path, factoryDefaultMode = None, autoCommit = None, autoRollback = None):
        if not isinstance(firmware_bytes_or_path, bytes):
            with open(firmware_bytes_or_path, 'rb') as firmware_file: # Using with open in Python is a best practice for handling files because it ensures that the file is properly closed
                firmware = firmware_file.read() 
        else:
            firmware = firmware_bytes_or_path
            
        json_request = self._BASE_JSON_REQUEST
        json_request["method"] = self.upgrade.__name__
        json_request["params"] = {}

        if factoryDefaultMode is not None:
            json_request["params"]["factoryDefaultMode"] = factoryDefaultMode.value if isinstance(factoryDefaultMode, FactoryDefaultModeType) else factoryDefaultMode
        if autoCommit is not None: 
            json_request["params"]["autoCommit"] = autoCommit.value if isinstance(autoCommit, AutoCommitType) else autoCommit
        if autoRollback is not None:
            json_request["params"]["autoRollback"] = autoRollback.value if isinstance(autoRollback, AutoRollbackType) else autoRollback

        json_data = json.dumps(json_request).encode("utf-8")

        return Request("POST", self.url, files=((None, json_data),(None,firmware)), auth=self.auth)    

    def commit(self):
        return self._create_no_params_request(self.commit.__name__)

    def roolback(self):
        return self._create_no_params_request(self.roolback.__name__)

    def purge(self):
        return self._create_no_params_request(self.purge.__name__)
    
    def factoryDefault(self, mode):
        params = {}
        if mode is not None:
            params["factoryDefaultMode"] = mode.value if isinstance(mode, FactoryDefaultModeType) else mode
        if params is not {}:
            return self._create_request_with_params(self.factoryDefault.__name__, params)
        else:
            return self._create_no_params_request(self.factoryDefault.__name__)

    def stopAuto(self):
        return self._create_no_params_request(self.stopAuto.__name__)
        
    def reboot(self):
        return self._create_no_params_request(self.reboot.__name__)
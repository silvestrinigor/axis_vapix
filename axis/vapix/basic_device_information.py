from abc import ABC, abstractmethod
from enum import Enum
from requests import Request
from typing import List
from dataclasses import asdict
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class DevicePropertyType(Enum):
    ARCHITECTURE = "Architecture"
    BRAND = "Brand"
    BUILD_DATE = "BuildDate"
    HARDWARE_ID = "hardwareId"
    PROD_FULL_NAME = "ProdFullName"
    PROD_NBR = "ProdNbr"
    PROD_SHORT_NAME = "ProdShortName"
    PROD_TYPE = "ProdType"
    PROD_VARIANT = "ProdVariant"
    SERIAL_NUMBER = "SerialNumber"
    SOC = "Soc"
    SOC_SERIAL_NUMBER = "SocSerialNumber"
    VERSION = "Version"
    WEB_URL = "WebURL"

class BasicDeviceInformationABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/basicdeviceinfo.cgi"
    API_DISCOVERY_ID = "basic-device-info"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "8.40"
    
    @abstractmethod
    def getProperties(self, propertyList: List[str | DevicePropertyType]):
        pass
    
    @abstractmethod
    def getAllProperties(self):
        pass
    
    @abstractmethod
    def getAllUnrestrictedProperties(self):
        pass

class BasicDeviceInformationRequest(BasicDeviceInformationABC, VapixRequestBuilderWithVersion):

    def getProperties(self, propertyList):
        if isinstance(propertyList, list) and all(isinstance(prop, DevicePropertyType) for prop in propertyList):
            propertyList = [str(prop.value) for prop in propertyList]
        return self._create_request_with_params(self.getProperties.__name__, {"propertyList": propertyList})    

    def getAllProperties(self):
        return self._create_no_params_request(self.getAllProperties.__name__)
    
    def getAllUnrestrictedProperties(self):
        return self._create_no_params_request(self.getAllUnrestrictedProperties.__name__)

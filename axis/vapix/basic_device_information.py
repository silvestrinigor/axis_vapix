from abc import ABC, abstractmethod
from enum import Enum
from requests import Request
from .requests import VapixApiRequest
from .api import VapixApiABC

class DevicePropertyType(Enum):
    NONE = None
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
    def getProperties(self, properties: list[str] | list[DevicePropertyType]):
        pass
    
    @abstractmethod
    def getAllProperties(self):
        pass
    
    @abstractmethod
    def getAllUnrestrictedProperties(self):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass

class BasicDeviceInformationRequest(BasicDeviceInformationABC, VapixApiRequest):

    def getProperties(self, properties: list[str] | list[DevicePropertyType]):
        if isinstance(properties, list) and all(isinstance(prop, DevicePropertyType) for prop in properties):
            properties = [prop.value for prop in properties]

        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getProperties",
            "params": {
                "propertyList": properties
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAllProperties(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getAllProperties"
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAllUnrestrictedProperties(self):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "getAllUnrestrictedProperties"
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions"
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
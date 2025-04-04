from abc import ABC, abstractmethod
from enum import Enum
from requests import Request
from requests.auth import AuthBase

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

class BasicDeviceInformationABC(ABC):
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

class BasicDeviceInformationRequest(BasicDeviceInformationABC):
    
    def __init__(self, host: str, port: int, auth: AuthBase | None = None, secure: bool = False, api_version: str = "1.0", context: str = ""):
        protocol = "https" if secure else "http"
        self.api_version = api_version
        self.context = context
        self.auth = auth
        self.url = f"{protocol}://{host}:{port}/{self.API_PATH}"

    def getProperties(self, properties: list[str] | list[DevicePropertyType]):
        if isinstance(properties, list[DevicePropertyType]):
            properties = [prop.value for prop in properties]
        
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getProperties",
            "params": {
                "propertyList": properties
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAllProperties(self):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getAllProperties",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getAllUnrestrictedProperties(self):
        json_request = {
            "apiVersion": self.api_version,
            "context": self.context,
            "method": "getAllUnrestrictedProperties",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)


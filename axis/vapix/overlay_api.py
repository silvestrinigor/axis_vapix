from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from enum import Enum
from requests import Request
from requests.auth import AuthBase
from .requests import VapixApiRequest
from .api import VapixApiABC

class OverlayColorType(Enum):
    NONE = None
    WHITE = "white"
    BLACK = "black"
    GREY = "grey"
    MOSAIC = "mosaic" # Hardware dependent
    CAMELEON = "cameleon" # Hardware dependent
    RED = "red"
    TRANSPARENT = "transparent"
    SEMI_TRANSPARENT = "semiTransparent"

class OverlayPositionType(Enum):
    NONE = None
    BOTTOM_RIGHT = "bottomRight"
    TOP_RIGHT = "topRight"
    BOTTOM = "bottom"
    TOP = "top"
    BOTTOM_LEFT = "bottomLeft"
    TOP_LEFT = "topleft"

class OverlayPositionCustomValue:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    def __repr__(self):
        return f"[{self.x}, {self.y}]"

@dataclass
class TextOverlay:
    camera:int | None= None
    fontSize:int | None = None
    identity: int | None = None
    indicator: str | None = None
    position: str | OverlayPositionCustomValue | None = None
    text: str | None = None
    textBgColor: str | None = None
    textColor: str | None = None
    textLength: int | None = None
    textOLColor: str | None = None
    visible: bool | None = None

@dataclass
class ImageOverlay:
    camera:int | None = None
    identity: int | None = None
    overlayPath: str | None = None
    position: str | OverlayPositionCustomValue | None = None
    visible: bool | None = None

class DynamicOverlayApiABC(VapixApiABC, ABC):
    API_PATH = "axis-cgi/dynamicoverlay/dynamicoverlay.cgi"
    FIRMWARE_LOWER_SUPPORTED_VERSION = "7.10"
    
    @abstractmethod
    def addImage(self, overlay: ImageOverlay | dict):
        pass
    
    @abstractmethod
    def addText(self, overlay: TextOverlay | dict):
        pass
    
    @abstractmethod
    def setImage(self, overlay: ImageOverlay | dict):
        pass
    
    @abstractmethod
    def setText(self, overlay: TextOverlay | dict):
        pass
    
    @abstractmethod
    def list(self, camera: int | None = None, identity: int | None = None):
        pass
    
    @abstractmethod
    def remove(self, identity: int):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
class DynamicOverlayApiRequest(DynamicOverlayApiABC, VapixApiRequest):
    
    def addImage(self, overlay: ImageOverlay | dict):
        if isinstance(overlay, ImageOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "addImage",
            "params": overlay,
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def addText(self, overlay: TextOverlay | dict):
        if isinstance(overlay, TextOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "addText",
            "params": overlay,
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setImage(self, overlay: ImageOverlay | dict):
        if isinstance(overlay, ImageOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setImage",
            "params": overlay,
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def setText(self, overlay: TextOverlay | dict):
        if isinstance(overlay, TextOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "setText",
            "params": overlay,
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)
    
    def list(self, camera: int | None = None, identity: int | None = None):        
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "list",
            "params": {
                
            }
        }
        
        if camera is not None:
            json_request["params"]["camera"] = camera
        if identity is not None:
            json_request["params"]["identity"] = identity
        
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def remove(self, identity: int):
        json_request = {
            "apiVersion": self.apiVersion,
            "context": self.context,
            "method": "remove",
            "params": {
                "identity": identity
            }
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

    def getSupportedVersions(self):
        json_request = {
            "context": self.context,
            "method": "getSupportedVersions",
        }
        return Request("POST", self.url, json=json_request, auth=self.auth)

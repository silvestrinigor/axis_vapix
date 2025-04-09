from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from enum import Enum
from requests import Request
from typing import Optional, List
from .requests import VapixRequestBuilderWithVersion
from .api import VapixApiABC

class OverlayColorType(Enum):
    WHITE = "white"
    BLACK = "black"
    GREY = "grey"
    MOSAIC = "mosaic" # Hardware dependent
    CAMELEON = "cameleon" # Hardware dependent
    RED = "red"
    TRANSPARENT = "transparent"
    SEMI_TRANSPARENT = "semiTransparent"

class OverlayPositionType(Enum):
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
    camera: Optional[int]= None
    fontSize: Optional[int] = None
    identity:  Optional[int] = None
    indicator: Optional[str] = None
    position: Optional[str | OverlayPositionCustomValue] = None
    text: Optional[str] = None
    textBgColor: Optional[str] = None
    textColor: Optional[str] = None
    textLength:  Optional[int] = None
    textOLColor: Optional[str] = None
    visible: Optional[bool] = None

@dataclass
class ImageOverlay:
    camera: Optional[int] = None
    identity:  Optional[int] = None
    overlayPath: Optional[str] = None
    position: Optional[str | OverlayPositionCustomValue] = None
    visible: Optional[bool] = None

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
    def list(self, camera:  Optional[int] = None, identity:  Optional[int] = None):
        pass
    
    @abstractmethod
    def remove(self, identity: int):
        pass
    
    @abstractmethod
    def getSupportedVersions(self):
        pass
    
class DynamicOverlayApiRequest(DynamicOverlayApiABC, VapixRequestBuilderWithVersion):
    
    def addImage(self, overlay):
        if isinstance(overlay, ImageOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        return self._create_request_with_params(self.addImage.__name__, overlay)
    
    def addText(self, overlay):
        if isinstance(overlay, TextOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        return self._create_request_with_params(self.addText.__name__, overlay)

    def setImage(self, overlay):
        if isinstance(overlay, ImageOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        return self._create_request_with_params(self.setImage.__name__, overlay)

    def setText(self, overlay):
        if isinstance(overlay, TextOverlay):
            overlay = self._remove_none_values(asdict(overlay))
        
        return self._create_request_with_params(self.setText.__name__, overlay)
    
    def list(self, camera = None, identity = None):        
        params = {}
        if camera is not None:
            params["camera"] = camera
        if identity is not None:
            params["identity"] = identity
        
        return self._create_request_with_params(self.list.__name__, params)

    def remove(self, identity):
        return self._create_request_with_params(self.remove.__name__, {"identity": identity})

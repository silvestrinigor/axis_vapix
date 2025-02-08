"""
https://developer.axis.com/vapix/network-video/overlay-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApi
from ..requests import AxisSession

PATH = "axis-cgi/dynamicoverlay/dynamicoverlay.cgi"
REQUEST_METHOD = "POST"
LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(7, 10, 0)

BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}

class MethodType(Enum):
    ADD_IMAGE = "addImage"
    ADD_TEXT = "addText"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    LIST = "list"
    REMOVE = "remove"
    SET_IMAGE = "setImage"
    SET_TEXT = "setText"
    GET_OVERLAY_CAPABILITIES = "getOverlayCapabilities"


class OverlayColorType(Enum):
    WHITE = "white"
    BLACK = "black"
    GREY = "grey"
    MOSAIC = "mosaic" # Hardware dependent
    CAMELEON = "cameleon" # Hardware dependent
    RED = "red"
    TRANSPARENT = "transparent"
    SEMI_TRANSPARENT = "semiTransparent"
    NONE = None


class OverlayPositionType(Enum):
    BOTTOM_RIGHT = "bottomRight"
    TOP_RIGHT = "topRight"
    BOTTOM = "bottom"
    TOP = "top"
    BOTTOM_LEFT = "bottomLeft"
    TOP_LEFT = "topleft"
    NONE = None


@dataclass
class OverlayPositionCustomValue:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


@dataclass
class TextOverlay:
    camera:int | None= None
    fontSize:int | None = None
    identity: int | None = None
    indicator: str | None = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    text: str | None = None
    textBgColor: OverlayColorType = OverlayColorType.NONE
    textColor: OverlayColorType = OverlayColorType.NONE
    textLength: int | None = None
    textOLColor: OverlayColorType = OverlayColorType.NONE
    visible: bool | None = None


@dataclass
class ImageOverlay:
    camera:int | None = None
    identity: int | None = None
    overlayPath: str | None = None
    position: OverlayPositionType | OverlayPositionCustomValue = OverlayPositionType.NONE
    visible: bool | None = None


class DynamicOverlayApi(IVapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH)
    
    def add_image(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.ADD_IMAGE, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def add_text(self, overlay: TextOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.ADD_TEXT, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def list(self, camera: str | None = None, identity: int | None = None):
        params = {}
        if camera != None: 
            params["camera"] = camera
        if identity != None: 
            params["identity"] = identity
        if params == {}:
            params = None
        
        body = self._create_body(MethodType.LIST, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def remove(self, identity: int):
        params = {"identity": identity}
        body = self._create_body(MethodType.REMOVE, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def set_image(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.SET_IMAGE, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def set_text(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.SET_TEXT, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def get_overlay_capabilities(self):
        body = self._create_body(MethodType.GET_OVERLAY_CAPABILITIES)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
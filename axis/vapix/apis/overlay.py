"""
https://developer.axis.com/vapix/network-video/overlay-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..api import IVapixApiClass, ApiVersion, FirmwareVersion
from ..requests import VapixRequest, AxisSession
from .. import utils

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


class DynamicOverlayApi(IVapixApiClass):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version)
    
    def add_image(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.ADD_IMAGE, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def add_text(self, overlay: TextOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.ADD_TEXT, params)
        request = self._create_request(body)
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
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def remove(self, identity: int):
        params = {"identity": identity}
        body = self._create_body(MethodType.REMOVE, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def set_image(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.SET_IMAGE, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def set_text(self, overlay: ImageOverlay):
        params = asdict(overlay)
        body = self._create_body(MethodType.SET_TEXT, params)
        request = self._create_request(body)
        response = self._send_request(request)
        return response

    def get_overlay_capabilities(self):
        body = self._create_body(MethodType.GET_OVERLAY_CAPABILITIES)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def get_supported_versions(self):
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body)
        response = self._send_request(request)
        return response
    
    def _create_request(self, json: dict):
        request = VapixRequest(
            method=REQUEST_METHOD, 
            url=self._base_url + PATH, 
            json=json, 
            auth=self.session.auth_type.value(
                self.session.credencial.username, 
                self.session.credencial.password
                )
            )
        return request
    
    def _create_body(self, method: MethodType, params: dict | None = None):
        body = BODY
        body["apiVersion"] = str(self.api_version)
        body["context"] = self.session.context
        body["method"] = method.value
        body["params"] = params
        body = utils.remove_none_values(body)
        return body
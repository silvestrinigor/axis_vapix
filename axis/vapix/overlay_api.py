from .apis import RequestAxisVapix
from .types import ApiPathType, RequestParamType, ParamType, MethodType
from .defaults import ImageOverlay, TextOverlay
from requests import Request

class RequestDynamicOverlayApi(RequestAxisVapix):
    """
    Property: Properties.API.HTTP.Version=3
    Property: Properties.DynamicOverlay.DynamicOverlay=yes
    Property: Properties.DynamicOverlay.Version=1.00
    Firmware: 7.10 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY

    def add_image(self, image_overlay: ImageOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ADD_IMAGE.value
        request_body[RequestParamType.PARAMS.value] = image_overlay.get_all_params()
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def add_text(self, text_overlay: TextOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ADD_TEXT.value
        request_body[RequestParamType.PARAMS.value] = text_overlay.get_all_params()
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def list(self, camera: str | None = None, identity: int | None = None):
        params = {}
        if camera != None: params[ParamType.CAMERA.value] = camera
        if identity != None: params[ParamType.IDENTITY.value] = identity
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.LIST.value
        if params != {}: request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def remove(self, identity: int | None = None):
        params = {
            ParamType.IDENTITY.value: identity
        }
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.REMOVE.value
        if params != {}: request_body[RequestParamType.PARAMS.value] = params
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_image(self, image_overlay: ImageOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_IMAGE.value
        request_body[RequestParamType.PARAMS.value] = image_overlay.get_all_params()
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_text(self, text_overlay: TextOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_TEXT.value
        request_body[RequestParamType.PARAMS.value] = text_overlay.get_all_params()
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_overlay_capabilities(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestOverlayModifiers(RequestAxisVapix): # TODO: Implement this class
    """
    Property: Properties.OverlayModifiers.OverlayModifiers="yes"
    Firmware: 5.1 and later
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_overlay_modifiers(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestTextOverlay(RequestAxisVapix): # TODO: Implement this class
    """
    To use this functionality set Image.I#.Text.TextEnabled to yes and set Image.I#.Text.String to contain the modifier #D.
    Access control: operator
    Method: GET
    """
    def __init__(self, host: str, port: int, api_version=None, context=None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

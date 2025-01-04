from requests import Request
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, ParamType, MethodType
from ..params import ImageOverlay, TextOverlay, ApiVersion

class RequestDynamicOverlayApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
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

class RequestOverlayModifiers(IRequestAxisVapix): # TODO: Implement this class

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

    def get_overlay_modifiers(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class RequestTextOverlay(IRequestAxisVapix): # TODO: Implement this class

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        raise NotImplementedError("This function is not implemented yet.")

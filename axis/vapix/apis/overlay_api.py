"""
https://developer.axis.com/vapix/network-video/overlay-api
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, ParamType, MethodType
from ..params import ImageOverlay, TextOverlay, ApiVersion, FirmwareVersion
from .. import request

DYNAMIC_OVERLAY_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(7, 10, 0)

class RequestDynamicOverlayApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_DYNAMIC_OVERLAY_API

    def add_image(self, image_overlay: ImageOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ADD_IMAGE.value
        request_body[RequestParamType.PARAMS.value] = image_overlay.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def add_text(self, text_overlay: TextOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.ADD_TEXT.value
        request_body[RequestParamType.PARAMS.value] = text_overlay.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def list(self, camera: str | None = None, identity: int | None = None):
        params = {}
        if camera != None: params[ParamType.CAMERA.value] = camera
        if identity != None: params[ParamType.IDENTITY.value] = identity
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.LIST.value
        if params != {}: request_body[RequestParamType.PARAMS.value] = params
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def remove(self, identity: int | None = None):
        params = {
            ParamType.IDENTITY.value: identity
        }
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.REMOVE.value
        if params != {}: request_body[RequestParamType.PARAMS.value] = params
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_image(self, image_overlay: ImageOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_IMAGE.value
        request_body[RequestParamType.PARAMS.value] = image_overlay.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_text(self, text_overlay: TextOverlay):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_TEXT.value
        request_body[RequestParamType.PARAMS.value] = text_overlay.get_all_params()
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_overlay_capabilities(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

class DynamicOverlayApi(RequestDynamicOverlayApi):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)

    def add_image(self, image_overlay: ImageOverlay, session: request.AxisVapixSession, auth):
        request = super().add_image(image_overlay)
        request.auth = auth
        self._send_request(request, session)

    def add_text(self, text_overlay: TextOverlay, session: request.AxisVapixSession, auth):
        request = super().add_text(text_overlay)
        request.auth = auth
        self._send_request(request, session)

    def list(self, session: request.AxisVapixSession, auth, camera: str | None = None, identity: int | None = None):
        request = super().list(camera, identity)
        request.auth = auth
        self._send_request(request, session)

    def remove(self, session: request.AxisVapixSession, auth, identity: int | None = None):
        request = super().remove(identity)
        request.auth = auth
        self._send_request(request, session)

    def set_image(self, image_overlay: ImageOverlay, session: request.AxisVapixSession, auth):
        request = super().set_image(image_overlay)
        request.auth = auth
        self._send_request(request, session)

    def set_text(self, text_overlay: TextOverlay, session: request.AxisVapixSession, auth):
        request = super().set_text(text_overlay)
        request.auth = auth
        self._send_request(request, session)

    def get_overlay_capabilities(self, session: request.AxisVapixSession, auth):
        request = super().get_overlay_capabilities()
        request.auth = auth
        self._send_request(request, session)

    async def async_add_image(self, image_overlay: ImageOverlay, session: request.AxisVapixAsyncSession, auth):
        request = super().add_image(image_overlay)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_add_text(self, text_overlay: TextOverlay, session: request.AxisVapixAsyncSession, auth):
        request = super().add_text(text_overlay)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_list(self, session: request.AxisVapixAsyncSession, auth, camera: str | None = None, identity: int | None = None):
        request = super().list(camera, identity)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_remove(self, session: request.AxisVapixAsyncSession, auth, identity: int | None = None):
        request = super().remove(identity)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_set_image(self, image_overlay: ImageOverlay, session: request.AxisVapixAsyncSession, auth):
        request = super().set_image(image_overlay)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_set_text(self, text_overlay: TextOverlay, session: request.AxisVapixAsyncSession, auth):
        request = super().set_text(text_overlay)
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

    async def async_get_overlay_capabilities(self, session: request.AxisVapixAsyncSession, auth):
        request = super().get_overlay_capabilities()
        request.auth = auth
        await session.post(request.url, json=request.json, headers=request.headers, auth=request.auth)

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

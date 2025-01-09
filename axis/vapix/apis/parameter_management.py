"""
https://developer.axis.com/vapix/network-video/parameter-management
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, ActionType, RequestUrlParamType
from ..params import FirmwareVersion
from ..handlers import AxisVapixAsyncResponseHandler
from .. import request

PARAMETER_MANAGEMENT_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(5, 0, 0)

class RequestParameterManagement(IRequestAxisVapix):

    def __init__(self, host: str, port: int, context: str | None = None):
        super().__init__(host, port, context)
        self._api_path_type = ApiPathType.AXIS_CGI_PARAM
    
    def list(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.LIST.value}{uri}")
        return request

    def list_definitions(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.LIST_DEFINITIONS.value}{uri}")
        return request
    
    def update(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.UPDATE.value}{uri}")
        return request
    
    def add(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.ADD.value}{uri}")
        return request
    
    def remove(self, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("GET", f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{ActionType.REMOVE.value}{uri}")
        return request
    
class ParameterManagement(RequestParameterManagement):
    def __init__(self, host, port, context = None):
        super().__init__(host, port, context)

    def list(self, session: request.AxisVapixSession, auth, **kwargs):
        request = super().list(**kwargs)
        request.auth = auth
        return self._send_request(request, session)

    def list_definitions(self, session: request.AxisVapixSession, auth, **kwargs):
        request = super().list_definitions(**kwargs)
        request.auth = auth
        return self._send_request(request, session)

    def update(self, session: request.AxisVapixSession, auth, **kwargs):
        request = super().update(**kwargs)
        request.auth = auth
        return self._send_request(request, session)

    def add(self, session: request.AxisVapixSession, auth, **kwargs):
        request = super().add(**kwargs)
        request.auth = auth
        return self._send_request(request, session)

    def remove(self, session: request.AxisVapixSession, auth, **kwargs):
        request = super().remove(**kwargs)
        request.auth = auth
        return self._send_request(request, session)

    async def list_async(self, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().list(**kwargs)
        request.auth = auth
        return await session.get(request.url, headers=request.headers, auth=request.auth)
    
    async def list_definitions_async(self, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().list_definitions(**kwargs)
        request.auth = auth
        return await session.get(request.url, headers=request.headers, auth=request.auth)
    
    async def update_async(self, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().update(**kwargs)
        request.auth = auth
        return await session.get(request.url, headers=request.headers, auth=request.auth)
    
    async def add_async(self, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().add(**kwargs)
        request.auth = auth
        return await session.get(request.url, headers=request.headers, auth=request.auth)
    
    async def remove_async(self, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().remove(**kwargs)
        request.auth = auth
        response = await session.get(request.url, headers=request.headers, auth=request.auth)
        return response
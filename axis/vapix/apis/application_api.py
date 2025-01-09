"""
https://developer.axis.com/vapix/applications/application-api
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, ActionType, RequestUrlParamType
from ..params import ApiVersion
from ..handlers import AxisVapixAsyncResponseHandler
from .. import request

class RequestAplicationApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_APPLICATIONS

    def upload(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def control_application(self, action: ActionType, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}?{RequestUrlParamType.ACTION.value}={action.value}{uri}")
        return request
    
    def start_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.START.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request

    def stop_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.STOP.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request

    def restart_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.RESTART.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request
    
    def remove_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.REMOVE.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request
    
    def set_configure_application(self, config_name:str, config_value: bool): # TODO: Test if this function works
        """
        Configure an application.
        :param config_name: String.
        :param config_value: Boolean.
        """
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONFIG.value}?{RequestUrlParamType.ACTION.value}={ActionType.SET.value}&{config_name}={config_value}")
        return request
    
    def get_configure_application(self, config_name: str): # TODO: Test if this function works
        """
        Get the configuration of an application.
        :param config_name: String.
        """
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONFIG.value}?{RequestUrlParamType.ACTION.value}={ActionType.GET.value}&{config_name}")
        return request
    
    def list(self): # TODO: Test if this function works
        request = self._create_request("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_LIST.value}")
        return request

class AplicationApi(RequestAplicationApi):
    def __init__(self, host, port, api_version, context = None):
        super().__init__(host, port, api_version, context)
        
    def upload(self, session: request.AxisVapixSession, auth):
        request = super().upload()
        request.auth = auth
        return self._send_request(request, session)
        
    def control_application(self, action: ActionType, session: request.AxisVapixSession, auth, **kwargs):
        request = super().control_application(action, **kwargs)
        request.auth = auth
        return self._send_request(request, session)
        
    def start_application(self, package: str, session: request.AxisVapixSession, auth, return_page = None):
        request = super().start_application(package, return_page)
        request.auth = auth
        return self._send_request(request, session)
        
    def stop_application(self, package: str, session: request.AxisVapixSession, auth, return_page = None):
        request = super().stop_application(package, return_page)
        request.auth = auth
        return self._send_request(request, session)
        
    def restart_application(self, package: str, session: request.AxisVapixSession, auth, return_page = None):
        request = super().restart_application(package, return_page)
        request.auth = auth
        return self._send_request(request, session)
        
    def remove_application(self, package: str, session: request.AxisVapixSession, auth, return_page = None):
        request = super().remove_application(package, return_page)
        request.auth = auth
        return self._send_request(request, session)
        
    def set_configure_application(self, config_name: str, config_value: bool, session: request.AxisVapixSession, auth):
        request = super().set_configure_application(config_name, config_value)
        request.auth = auth
        return self._send_request(request, session)
        
    def get_configure_application(self, config_name: str, session: request.AxisVapixSession, auth):
        request = super().get_configure_application(config_name)
        request.auth = auth
        return self._send_request(request, session)
    
    def list(self, session: request.AxisVapixSession, auth):
        request = super().list()
        request.auth = auth
        return self._send_request(request, session)

    async def async_upload(self, session: request.AxisVapixAsyncSession, auth):
        request = super().upload()
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_control_application(self, action: ActionType, session: request.AxisVapixAsyncSession, auth, **kwargs):
        request = super().control_application(action, **kwargs)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_start_application(self, package: str, session: request.AxisVapixAsyncSession, auth, return_page = None):
        request = super().start_application(package, return_page)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_stop_application(self, package: str, session: request.AxisVapixAsyncSession, auth, return_page = None):
        request = super().stop_application(package, return_page)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_restart_application(self, package: str, session: request.AxisVapixAsyncSession, auth, return_page = None):
        request = super().restart_application(package, return_page)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_remove_application(self, package: str, session: request.AxisVapixAsyncSession, auth, return_page = None):
        request = super().remove_application(package, return_page)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_set_configure_application(self, config_name: str, config_value: bool, session: request.AxisVapixAsyncSession, auth):
        request = super().set_configure_application(config_name, config_value)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_get_configure_application(self, config_name: str, session: request.AxisVapixAsyncSession, auth):
        request = super().get_configure_application(config_name)
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
    
    async def async_list(self, session: request.AxisVapixAsyncSession, auth):
        request = super().list()
        request.auth = auth
        response = await session.post(request.url, headers=request.headers, auth=request.auth)
        AxisVapixAsyncResponseHandler(response).handle_errors()
        return response
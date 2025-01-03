"""
https://developer.axis.com/vapix/applications/application-api
"""

from ..request import AxisRequest
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, ActionType, RequestUrlParamType
from ..params import ApiVersion

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
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}?{RequestUrlParamType.ACTION.value}={action.value}{uri}")
        return request
    
    def start_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.START.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request

    def stop_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.STOP.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request

    def restart_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.RESTART.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request
    
    def remove_application(self, package: str, return_page: str | None = None): # TODO: Test if this function works
        uri = f"&{RequestUrlParamType.ACTION.value}={ActionType.REMOVE.value}&package={package}"
        if return_page != None: uri += f"&return_page={return_page}"
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL.value}{uri}")
        return request
    
    def set_configure_application(self, config_name:str, config_value: bool): # TODO: Test if this function works
        """
        Configure an application.
        :param config_name: String.
        :param config_value: Boolean.
        """
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONFIG.value}?{RequestUrlParamType.ACTION.value}={ActionType.SET.value}&{config_name}={config_value}")
        return request
    
    def get_configure_application(self, config_name: str): # TODO: Test if this function works
        """
        Get the configuration of an application.
        :param config_name: String.
        """
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_CONFIG.value}?{RequestUrlParamType.ACTION.value}={ActionType.GET.value}&{config_name}")
        return request
    
    def list(self): # TODO: Test if this function works
        request = AxisRequest("POST", f"http://{self._host}:{self._port}/{ApiPathType.AXIS_CGI_APPLICATIONS_LIST.value}")
        return request


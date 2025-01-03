from .apis import RequestAxisVapix
from .types import ApiPathType, ActionType, RequestUrlParamType
import io
from requests import Request

class RequestAplicationApi(RequestAxisVapix):
    """
    Property: Properties.EmbeddedDevelopment.Version exists.
    list.cgi requries:
    Property: Properties.EmbeddedDevelopment.Version=1.20 and later.
    """
    def __init__(self, host: str, port: int, context = None):
        super().__init__(host, port, context=context)

    def upload(self, file_obj: io.BufferedReader): # TODO: Test if this function works
        self._api_path_type = ApiPathType.AXIS_CGI_APPLICATIONS_UPLOAD
        files = {'file': ('application_file.bin', file_obj, 'application/octet-stream')}
        request = Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", files=files)
        self._api_path_type = ApiPathType.NONE
        return request
    
    def control_application(self, action: ActionType, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        self._api_path_type = ApiPathType.AXIS_CGI_APPLICATIONS_CONTROL
        request = Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}?{RequestUrlParamType.ACTION.value}={action.value}{uri}")
        self._api_path_type = ApiPathType.NONE
        return request
    
    def configure_application(self, action: ActionType, config_name:str, config_value): # TODO: Test if this function works
        uri = ""
        self._api_path_type = ApiPathType.AXIS_CGI_APPLICATIONS_CONFIG
        request = Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}?{RequestUrlParamType.ACTION.value}={action.value}&{config_name}={config_value}")
        self._api_path_type = ApiPathType.NONE
        return request
    
    def list(self): # TODO: Test if this function works
        self._api_path_type = ApiPathType.AXIS_CGI_APPLICATIONS_LIST
        request = Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}")
        self._api_path_type = ApiPathType.NONE
        return request

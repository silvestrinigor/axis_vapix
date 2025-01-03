from .apis import RequestAxisVapix
from .types import ApiPathType, RequestParamType, MethodType, ParamType
from requests import Request

class RequestLoiteringGuard(RequestAxisVapix):
    """
    Software: EmbeddedDevelopment version 2.13 or higher is required for the ACAP to work.
    Property: Properties.EmbeddedDevelopment.Version=2.13
    In order to check if the ACAP is installed, use /axis-cgi/applications/list.cgi, which shows the status of all installed ACAPs. It also lists the url to the configuration page and the license state of the ACAP.
    """
    def __init__(self, host: str, port: int, api_version: str = None, context = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.LOCAL_LOITERING_GUARD
    
    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def send_alarm(self, profile: int):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.SEND_ALARM_EVENT.value
        request_body[RequestParamType.PARAMS.value] = {ParamType.PROFILE.value: profile}
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_configuration(self):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_CONFIGURATION_CAPABILITIES.value
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_supported_versions(self):
        return super()._get_supported_versions()

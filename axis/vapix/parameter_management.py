from .apis import RequestAxisVapix
from .types import ApiPathType, ActionType, RequestUrlParamType
from requests import Request

class RequestParameterManagement(RequestAxisVapix):
    """
    Property: Properties.API.HTTP.Version=3
    Firmware: 5.00 and later.
    """
    def __init__(self, host, port, context = None):
        super().__init__(host, port, context)
        self._api_path_type = ApiPathType.AXIS_CGI_PARAM

    def get_request(self, action: ActionType, **kwargs): # TODO: Test if this function works
        uri = ""
        for key, value in kwargs.items():
            uri += f"&{key}={value}"
        if action == ActionType.LIST:
            request_method = "GET"
        else:
            request_method = "POST"
        request = Request(request_method, f"http://{self._host}:{self._port}/{self._api_path_type.value}{RequestUrlParamType.ACTION.value}{action.value}{uri}")
        return request

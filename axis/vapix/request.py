import requests
import requests.auth
from .defaults import ApiPathType
from .defaults import MethodType
from .defaults import RequestParamType
from .defaults import FactoryDefaultModeType
from abc import ABC, abstractmethod

class ApiVersion:
    def __init__(self, major:int, minor:int):
        self.major:int = major
        self.minor:int = minor
    def __repr__(self):
        return f"{self.major}.{self.minor}"
    def __str__(self):
        return f"{self.major}.{self.minor}"  
  
class JsonRequestConfig:
    def __init__(self, method: MethodType, context: str, version: ApiVersion | None= None, params: dict | None = None, channel: int | None= None, capture_mode_id: int| None= None, factory_default_mode: FactoryDefaultModeType | None= None):
        self.json_request_config = {
            RequestParamType.CONTEXT.value: context,
            RequestParamType.METHOD.value: method.value
        }
        if version != None:
            self.json_request_config[RequestParamType.API_VERSION.value] = version.__str__()
        if params != None:
            self.json_request_config[RequestParamType.PARAMS.value] = params
        if channel != None:
            self.json_request_config[RequestParamType.CHANNEL.value] = channel
        if capture_mode_id != None:
            self.json_request_config[RequestParamType.CAPTURE_MODE_ID.value] = capture_mode_id            
        if factory_default_mode != None:
            self.json_request_config[RequestParamType.FACTORY_DEFAULT_MODE.value] = factory_default_mode                      
    def get_config(self):
        return self.json_request_config
    def __repr__(self):
        return self.json_request_config
    def __str__(self):
        return self.json_request_config
    
class AxisRequest(ABC):
    _username: str
    _password: str
    _url: str
    api_version: ApiVersion
    request_context: str
    
    @abstractmethod
    def request_post(self, api: ApiPathType, request_config: JsonRequestConfig):
        return requests.Response
    @abstractmethod
    def request_get(self, api: ApiPathType, request_config: JsonRequestConfig):
        return requests.Response

class AxisDefaultRequestMaker(AxisRequest):
    def __init__(self, host: str, port:int, username: str, password: str):
        self._username = username
        self._password = password
        self._url = f"http://{host}:{port}/"
        self.timeout:int = 10
        self.auth: requests.auth = requests.auth.HTTPDigestAuth(username, password)
        self.api_version: ApiVersion = ApiVersion(1,1)
        self.request_context: str = ""
    
    def request_post(self, api: ApiPathType, request_config: JsonRequestConfig):
        return requests.post(url= self._url + api.value, auth= self.auth, json= request_config.get_config())

    def request_get(self, api: ApiPathType, request_config: JsonRequestConfig):
        return requests.get(url= self._url + api.value, auth= self.auth, json= request_config.get_config())

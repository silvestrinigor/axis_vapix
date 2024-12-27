import gevent.monkey
gevent.monkey.patch_all(thread=False, select=False)
from abc import ABC, abstractmethod
from .types import RequestMethod, RequestParamType
from requests import Response
from grequests import AsyncRequest

class IRequestBuilder(ABC):
    method: "RequestMethod"
    url: str
    headers: dict
    params: dict
    data: dict
    json_data: dict
    files: dict
    timeout: int
    auth: type

    @abstractmethod
    def set_headers(self, headers: dict) -> "IRequestBuilder":
        pass

    @abstractmethod
    def set_params(self, params: dict) -> "IRequestBuilder":
        pass

    @abstractmethod
    def set_data(self, data: dict) -> "IRequestBuilder":
        pass

    @abstractmethod
    def set_json(self, json_data: dict) -> "IRequestBuilder":
        pass

    @abstractmethod
    def set_files(self, files: dict) -> "IRequestBuilder":
        pass

    @abstractmethod
    def set_auth(self, username: str, password: str, auth_type: type) -> "IRequestBuilder":
        pass

    @abstractmethod
    def get_kwargs(self) -> dict:
        pass

class IRequestMaker(ABC):

    @abstractmethod
    def send_request(self, request_builder: IRequestBuilder) -> Response:
        pass

    @abstractmethod
    def get_async_request(self, request_builder: IRequestBuilder) -> AsyncRequest:
        pass

    @abstractmethod
    def send_async_requests(self, request_list: list) -> list:
        pass

class IAxisRequestBody(ABC):
    request_body: dict

    @abstractmethod
    def add_or_set_request_param(self, param_type: RequestParamType, value) -> None:
        pass

    @abstractmethod
    def get_request_body(self) -> dict:
        pass

class IParamConfig(ABC):
    
    @abstractmethod
    def get_all_params(self) -> dict:
        pass

class IAxisRequestManager(ABC):
    device: object
    request_context: str
    request_api_version: object
    _request_auth: type
    
    @abstractmethod
    def make_request_build(self):
        pass


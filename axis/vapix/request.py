import requests
import requests.auth
import grequests
from .types import RequestMethod
from .abc_classes import IRequestBuilder, IRequestMaker

class RequestBuilder(IRequestBuilder):
    def __init__(self, method: RequestMethod, url):
        self.method: RequestMethod = method.value
        self.url = url
        self.headers = None
        self.params = None
        self.data = None
        self.json_data = None
        self.files = None
        self.timeout = None
        self.auth = None

    def set_headers(self, headers: dict):
        if self.headers == None:
            self.headers = {}
        self.headers.update(headers)
        return self

    def set_params(self, params: dict):
        if self.params == None:
            self.params = {}
        self.params.update(params)
        return self

    def set_data(self, data: dict):
        self.data = data
        return self

    def set_json(self, json_data: dict):
        self.json_data = json_data
        return self

    def set_files(self, files: dict):
        self.files = files
        return self

    def set_auth(self, username: str, password: str, auth_type: type):
        if not issubclass(auth_type, requests.auth.AuthBase):
            raise ValueError("auth_type must be a subclass of requests.auth.AuthBase")
        self.auth = auth_type(username, password)
        return self

    def get_kwargs(self):
        request_kwargs = {
            'headers': self.headers, 
            'params': self.params,
            'data': self.data, 
            'json': self.json_data,
            'files': self.files, 
            'timeout': self.timeout,
            'auth': self.auth
        }
        request_kwargs = {key: value for key, value in request_kwargs.items() if value is not None}
        return request_kwargs
    
    def send_request(self):
        return RequestMaker().send_request(self.get_kwargs())

class RequestMaker(IRequestMaker):
    def __init__(self):
        pass

    def send_request(self, request_build: RequestBuilder) -> requests.Response:
        return requests.request(request_build.method, request_build.url, **request_build.get_kwargs())

    def get_async_request(self, request_builder: RequestBuilder) -> grequests.AsyncRequest:
        return grequests.request(request_builder.method, request_builder.url, **request_builder.get_kwargs())

    def send_async_requests(self, request_list: list[grequests.AsyncRequest]) -> list:
        return grequests.map(request_list)

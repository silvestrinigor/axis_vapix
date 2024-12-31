from .types import RequestMethod

class RequestBuilder:
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


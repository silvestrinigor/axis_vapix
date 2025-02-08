from enum import Enum
from .requests import AxisSession, VapixRequest, VapixResponse
from .connection import ApiVersion
from . import utils

class IVapixApiClass:
    def __init__(self, session: AxisSession, api_version: ApiVersion, path: str):
        self.session = session
        self.api_version = api_version
        self._base_url = f"http://{session.server.host}:{session.server.port}/"
        self.path = path

    def _send_request(self, request: VapixRequest):
        prepared_request = request.prepare()
        response = self.session.send(request=prepared_request)
        response: VapixResponse
        return response

    def _create_request(self, json: dict, request_method: str):
        request = VapixRequest(
            method=request_method, 
            url=self._base_url + self.path, 
            json=json, 
            auth=self.session.auth_type.value(
                self.session.credencial.username, 
                self.session.credencial.password
                )
            )
        return request
    
    def _create_body(self, method: Enum, params: dict | None = None):
        body = body
        body["apiVersion"] = str(self.api_version)
        body["context"] = self.session.context
        body["method"] = method.value
        body["params"] = params
        body = utils.remove_none_values(body)
        return body
import requests
import requests.auth
from enum import Enum
from .connection import AxisServer, AxisCredencial

class VapixRequest(requests.Request):
    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        super().__init__(method, url, headers, files, data, params, auth, cookies, hooks, json)


class VapixResponse(requests.Response):
    pass


class AuthType(Enum):
    BASIC_AUTH = requests.auth.HTTPBasicAuth
    DIGEST_AUTH = requests.auth.HTTPDigestAuth
    

class AxisSession(requests.Session):
    def __init__(self, server: AxisServer, credencial: AxisCredencial, auth_type: AuthType = AuthType.DIGEST_AUTH, context: str | None = None):
        super().__init__()
        self.server: AxisServer = server
        self.credencial: AxisCredencial = credencial
        self.context: str = context
        self.auth_type: AuthType = auth_type
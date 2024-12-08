from . import methods
from . import request
from . import handlers
import json

class Device:
    def __init__(self, host:str, port: int, username: str, password: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
    
    def is_this_api_supported(self, api_id: str, api_version: str=None):
        pass
    
    def _update_supported_api_list():
        pass
from requests import Response
from . import defaults
import json

def is_response_with_error(response: Response) -> bool:
    json.loads(response.text)
    if defaults.ResponseType.ERROR.value in response:
        return True
    else:
        return False

class AxisApiResponseHandler:
    def __init__(self, response: Response):
        self.response = response
        self.json_content = json.loads(response.text)
    
    def get_used_method(self):
        return self.json_content[defaults.ResponseType.METHOD.value]
    
    def get_api_version(self):
        return self.json_content[defaults.ResponseType.API_VERSION.value]
    
    def get_response_data(self):
        return self.json_content[defaults.ResponseType.DATA.value]
    
    def is_response_with_error(self):
        return is_response_with_error(self.response)
    

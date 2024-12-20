from requests import Response
from . import defaults
from . import request
from .utils import get_apiversion_type_from_string
import json
from datetime import datetime

def is_response_with_error(response: Response) -> bool:
    if defaults.ResponseType.ERROR.value in response.text:
        return True
    else:
        return False

class AxisResponseHandler:
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
    
class DateTimeInfoResponseHandler(AxisResponseHandler):
    def __init__(self, response):
        super().__init__(response)
    
    @property
    def date_time(self):
        data = self.get_response_data()
        return datetime.fromisoformat(data[defaults.ResponseDataType.DATE_TIME.value].rstrip("Z"))
    
    @property
    def local_date_time(self):
        data = self.get_response_data()
        return datetime.fromisoformat(data[defaults.ResponseDataType.LOCAL_DATE_TIME.value].rstrip("Z"))
    
    @property
    def time_zone(self):
        data = self.get_response_data()
        return data[defaults.ResponseDataType.TIME_ZONE.value]
    
    @property
    def is_dst_enable(self):
        data = self.get_response_data()
        return bool(data[defaults.ResponseDataType.DST_ENABLE.value])

class ApisInfoResponseHandler(AxisResponseHandler):
    def __init__(self, response):
        super().__init__(response)
    
    @property
    def api_list(self):
        api_list: list[dict] = []
        json_data_info = self.get_response_data()[defaults.ResponseDataType.API_LIST.value]
        for api_json in json_data_info:
            api_list.append(api_json)
        return api_list
    
    def is_this_api_supported(self, api_type: defaults.ApiType):
        api_list = self.response.json().get(defaults.ResponseType.DATA.value, {}).get(defaults.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[defaults.ResponseDataApiType.ID.value] == api_type.value:
                return True
        return False

    def is_this_api_version_supported(self, api_type: defaults.ApiType, api_version: request.ApiVersion):
        api_list = self.response.json().get(defaults.ResponseType.DATA.value, {}).get(defaults.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[defaults.ResponseDataApiType.ID.value] == api_type.value and api[defaults.ResponseDataApiType.VERSION.value] == api_version.__str__():
                return True
        return False

    def get_supported_api_version(self, api_type: defaults.ApiType):
        api_list = self.response.json().get(defaults.ResponseType.DATA.value, {}).get(defaults.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[defaults.ResponseDataApiType.ID.value] == api_type.value:
                return get_apiversion_type_from_string(api[defaults.ResponseDataApiType.VERSION.value])
        raise defaults.AxisVapixVersionNotSupportedExeption()
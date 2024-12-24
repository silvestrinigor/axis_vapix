from requests import Response
from . import types
from . import request
from .utils import get_apiversion_type_from_string
import json
from datetime import datetime

def is_response_with_error(response: Response) -> bool:
    if types.ResponseType.ERROR.value in response.text:
        return True
    else:
        return False

class AxisResponseHandler:
    def __init__(self, response: Response):
        self.response = response
        self.json_content = json.loads(response.text)
    
    def get_used_method(self):
        return self.json_content[types.ResponseType.METHOD.value]
    
    def get_api_version(self):
        return self.json_content[types.ResponseType.API_VERSION.value]
    
    def get_response_data(self):
        return self.json_content[types.ResponseType.DATA.value]
    
    def is_response_with_error(self):
        return is_response_with_error(self.response)
    
class DateTimeInfoResponseHandler(AxisResponseHandler):
    def __init__(self, response):
        super().__init__(response)
    
    @property
    def date_time(self):
        data = self.get_response_data()
        return datetime.fromisoformat(data[types.ResponseDataType.DATE_TIME.value].rstrip("Z"))
    
    @property
    def local_date_time(self):
        data = self.get_response_data()
        return datetime.fromisoformat(data[types.ResponseDataType.LOCAL_DATE_TIME.value].rstrip("Z"))
    
    @property
    def time_zone(self):
        data = self.get_response_data()
        return data[types.ResponseDataType.TIME_ZONE.value]
    
    @property
    def is_dst_enable(self):
        data = self.get_response_data()
        return bool(data[types.ResponseDataType.DST_ENABLE.value])

class ApisInfoResponseHandler(AxisResponseHandler):
    def __init__(self, response):
        super().__init__(response)
    
    @property
    def api_list(self):
        api_list: list[dict] = []
        json_data_info = self.get_response_data()[types.ResponseDataType.API_LIST.value]
        for api_json in json_data_info:
            api_list.append(api_json)
        return api_list
    
    def is_this_api_supported(self, api_type: types.ApiType):
        api_list = self.response.json().get(types.ResponseType.DATA.value, {}).get(types.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[types.ResponseDataApiType.ID.value] == api_type.value:
                return True
        return False

    def is_this_api_version_supported(self, api_type: types.ApiType, api_version: request.ApiVersion):
        api_list = self.response.json().get(types.ResponseType.DATA.value, {}).get(types.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[types.ResponseDataApiType.ID.value] == api_type.value and api[types.ResponseDataApiType.VERSION.value] == api_version.__str__():
                return True
        return False

    def get_supported_api_version(self, api_type: types.ApiType):
        api_list = self.response.json().get(types.ResponseType.DATA.value, {}).get(types.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[types.ResponseDataApiType.ID.value] == api_type.value:
                return get_apiversion_type_from_string(api[types.ResponseDataApiType.VERSION.value])
        raise types.AxisVapixVersionNotSupportedExeption()
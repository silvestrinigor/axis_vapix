from . import methods
from . import request
from . import handlers
from . import defaults
import json
from datetime import datetime

class Device:
    def __init__(self, host:str, port: int, username: str, password: str):
        self._request_maker = request.AxisRequestMaker(host=host, port=port, username=username, password=password)
        self._apis_list_response: request.requests.Response
        self._update_apis_json_info()

    @property
    def serial_number(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [defaults.DevicePropertyType.SERIAL_NUMBER]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.SERIAL_NUMBER.value]

    @property
    def version(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [defaults.DevicePropertyType.VERSION]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.VERSION.value]
    
    @property
    def type(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [defaults.DevicePropertyType.PROD_TYPE]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.PROD_TYPE.value]
    
    @property
    def date_time(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).date_time

    @date_time.setter
    def date_time(self, date_time: datetime):
        response = methods.set_date_time(self._request_maker, date_time=date_time)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return

    @property
    def local_date_time(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).local_date_time

    @property
    def time_zone(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).time_zone
    
    @time_zone.setter
    def time_zone(self, time_zone: defaults.TimeZoneType):
        response = methods.set_time_zone(self._request_maker, time_zone=time_zone)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return
    
    @property
    def is_time_dst_enable(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).is_dst_enable

    def set_posix_time_zone(self, posix_time_zone, enable_dst: bool):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(defaults.ApiType.AXIS_CGI_TIME)
        response = methods.set_posix_time_zone(self._request_maker, posix_time_zone=posix_time_zone, enable_dst=enable_dst)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return
    
    def is_this_api_supported(self, api_type: defaults.ApiType):
        response = methods.get_api_list(self._request_maker)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        api_list = response.json().get(defaults.ResponseType.DATA.value, {}).get(defaults.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[defaults.ResponseDataApiType.ID.value] == api_type.value:
                return True
        return False

    def is_this_api_version_supported(self, api_type: defaults.ApiType, api_version: request.ApiVersion):
        response = methods.get_api_list(self._request_maker)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        api_list = response.json().get(defaults.ResponseType.DATA.value, {}).get(defaults.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[defaults.ResponseDataApiType.ID.value] == api_type.value and api[defaults.ResponseDataApiType.VERSION.value] == api_version.__str__():
                return True
        return False
    
    def _update_apis_json_info(self):
        self._apis_list_response =  methods.get_api_list(self._request_maker)
        
        

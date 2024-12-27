from . import methods
from . import request
from . import handlers
from . import types
import json
from datetime import datetime

class Device:
    def __init__(self, host:str, port: int, username: str, password: str):
        self._request_maker = request.AxisDefaultRequestMaker(host=host, port=port, username=username, password=password)
        self._apis_list_response: request.requests.Response
        self._update_apis_json_info()

    @property
    def serial_number(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [types.DevicePropertyType.SERIAL_NUMBER]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[types.ResponseType.DATA.value][types.ResponseDataType.PROPERTY_LIST.value][types.DevicePropertyType.SERIAL_NUMBER.value]

    @property
    def version(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [types.DevicePropertyType.VERSION]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[types.ResponseType.DATA.value][types.ResponseDataType.PROPERTY_LIST.value][types.DevicePropertyType.VERSION.value]
    
    @property
    def type(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_BASIC_DEVICE_INFO)
        properties = [types.DevicePropertyType.PROD_TYPE]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[types.ResponseType.DATA.value][types.ResponseDataType.PROPERTY_LIST.value][types.DevicePropertyType.PROD_TYPE.value]
    
    @property
    def date_time(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).date_time

    @date_time.setter
    def date_time(self, date_time: datetime):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.set_date_time(self._request_maker, date_time=date_time)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return

    @property
    def local_date_time(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).local_date_time

    @property
    def time_zone(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).time_zone
    
    @time_zone.setter
    def time_zone(self, time_zone: types.TimeZoneType):
        response = methods.set_time_zone(self._request_maker, time_zone=time_zone)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return
    
    @property
    def is_time_dst_enable(self):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.get_date_time_info(self._request_maker)
        return handlers.DateTimeInfoResponseHandler(response=response).is_dst_enable

    def set_posix_time_zone(self, posix_time_zone, enable_dst: bool):
        self._request_maker.api_version = handlers.ApisInfoResponseHandler(self._apis_list_response).get_supported_api_version(types.ApiType.AXIS_CGI_TIME)
        response = methods.set_posix_time_zone(self._request_maker, posix_time_zone=posix_time_zone, enable_dst=enable_dst)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return
    
    def is_this_api_supported(self, api_type: types.ApiType):
        response = methods.get_api_list(self._request_maker)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        api_list = response.json().get(types.ResponseType.DATA.value, {}).get(types.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[types.ResponseDataApiType.ID.value] == api_type.value:
                return True
        return False

    def is_this_api_version_supported(self, api_type: types.ApiType, api_version: request.ApiVersion):
        response = methods.get_api_list(self._request_maker)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        api_list = response.json().get(types.ResponseType.DATA.value, {}).get(types.ResponseDataType.API_LIST.value, [])
        for api in api_list:
            if api[types.ResponseDataApiType.ID.value] == api_type.value and api[types.ResponseDataApiType.VERSION.value] == api_version.__str__():
                return True
        return False
    
    def _update_apis_json_info(self):
        self._request_maker.api_version = request.ApiVersion(1,0)
        self._apis_list_response =  methods.get_api_list(self._request_maker)
        if handlers.is_response_with_error(self._apis_list_response) or self._apis_list_response.status_code != 200:
            print(str(self._apis_list_response.status_code) + self._apis_list_response.text)
            raise Exception

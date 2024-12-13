from . import methods
from . import request
from . import handlers
from . import defaults
import json

class Device:
    def __init__(self, host:str, port: int, username: str, password: str):
        self._request_maker = request.AxisRequestMaker(host=host, port=port, username=username, password=password)

    @property
    def serial_number(self):
        properties = [defaults.DevicePropertyType.SERIAL_NUMBER]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.SERIAL_NUMBER.value]

    @property
    def version(self):
        properties = [defaults.DevicePropertyType.VERSION]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.VERSION.value]
    
    @property
    def type(self):
        properties = [defaults.DevicePropertyType.PROD_TYPE]
        response = methods.get_properties(axis_request=self._request_maker, properties=properties)
        if response.status_code != 200 or handlers.is_response_with_error(response=response) == True:
            raise Exception()
        return json.loads(response.text)[defaults.ResponseType.DATA.value][defaults.ResponseDataType.PROPERTY_LIST.value][defaults.DevicePropertyType.PROD_TYPE.value]
    
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
        
class Camera(Device):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)

class Bridge(Device):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)
        
        

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
        if response.status_code != 200 | handlers.is_response_with_error(response=response) == True:
            raise Exception("Exeption")
        return json.loads(response.text)["data"]["propertyList"]["SerialNumber"]
        
    def is_this_api_supported(self, api_id: str, api_version: str):
        pass

class Camera(Device):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)

class Bridge(Device):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)
        
        

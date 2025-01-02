from axis.vapix import apis
from axis.vapix.types import RequestUrlParamType, ActionType
from axis.vapix.exeptions import AxisVapixExeption, AxisVapixVersionNotSupportedExeption
import requests
import requests.auth

class Device:
    def __init__(self, host: str, port: int, username: str, password: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        
        self._session = requests.Session()
        self._session.auth = requests.auth.HTTPDigestAuth(self._username, self._password)

        self._firmware_version = None
        self._serial_number = None
        
        self._firmware_management_version = None
        
        self._is_device_properties_info_avaliable: bool = False
        
        

    def get_properties(self):
        kewargs = {
           RequestUrlParamType.GROUP.value: "root.Properties",
        }
        request = apis.RequestParameterManagement(self._host, self._port).get_request(ActionType.LIST, **kewargs)
        request.auth = self._session.auth
        requestp = request.prepare()
        response = self._session.send(requestp)
        if response.status_code != 200:
            raise AxisVapixExeption(f"Error: {response.status_code} - {response.text}")
        if apis.ResponseAxisCgi(response).is_textplain_response_with_error():
            raise AxisVapixExeption(response.text)
        # Split the text into lines
        lines = response.text.strip().split("\n")
        # Loop through each line and process it
        for line in lines:
            # Split the line by '=' to separate the property path and value
            key, value = line.split('=')
            if key == "root.Properties.System.SerialNumber":
                self._serial_number = value
            if key == "root.Properties.Firmware.Version":
                self._firmware_version = value
            if key == "root.Properties.FirmwareManagement.Version":
                self._firmware_management_version = value
                
        self._is_device_properties_info_avaliable = True


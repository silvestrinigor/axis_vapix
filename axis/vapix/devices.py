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
        self._prod_type = None
        self._prod_nbr = None


    def get_device_properties(self):
        """
        Property: Properties.API.HTTP.Version=3
        Firmware: 5.00 and later.
        """
        kewargs = {
           RequestUrlParamType.GROUP.value: "root.Properties",
           RequestUrlParamType.GROUP.value: "root.Brand"
        }
        request = apis.RequestParameterManagement(self._host, self._port).get_request(ActionType.LIST, **kewargs)
        requestp = request.prepare()
        response = self._session.send(requestp)
        if response.status_code != 200:
            raise AxisVapixExeption(f"Error: {response.status_code} - {response.text}")
        if apis.ResponseAxisCgi(response).is_textplain_response_with_error():
            raise AxisVapixExeption(response.text)
        print(response.text)
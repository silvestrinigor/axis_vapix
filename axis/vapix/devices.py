from axis.vapix import apis
from axis.vapix.types import RequestUrlParamType, ActionType
from axis.vapix.exeptions import AxisVapixExeption, AxisVapixVersionNotSupportedExeption
import requests
import requests.auth
from packaging.version import Version
from utils import get_firmwareversion_type_from_string
from utils import get_apiversion_type_from_string
from datetime import datetime

class Device:
    def __init__(self, host: str, port: int, username: str, password: str):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._session = requests.Session()
        self._session.auth = requests.auth.HTTPDigestAuth(self._username, self._password)
        self._firmware_version: Version | None = None
        self._serial_number: str | None = None
        self._firmware_management_version: Version | None = None
        self._is_basic_device_info_supported: bool = False
        self._is_api_discovey_supported: bool = False
        self._is_device_properties_info_avaliable: bool = False
    
    @property
    def firmware_version(self) -> Version:
        self._ensure_device_properties_available()
        return self._firmware_version
    
    @property
    def serial_number(self) -> str:
        self._ensure_device_properties_available()
        return self._serial_number
    
    @property
    def date_time(self) -> datetime:
        self._ensure_device_properties_available()
        request = apis.RequestTimeApi(self._host, self._port).get_date_time_info()
        request.auth = self._session.auth
        response = self._session.send(request.prepare())
        self._ensure_response_status_ok(response)
        self._ensure_response_textplain(response)
        print(response.text)

    def _ensure_device_properties_available(self):
        if not self._is_device_properties_info_avaliable:
            raise AxisVapixExeption("Device properties not available. Call get_properties() first.")
    
    def _ensure_response_status_ok(self, response: requests.Response):
        if response.status_code != 200:
            raise AxisVapixExeption(f"Error: {response.status_code} - {response.text}")

    def _ensure_response_textplain(self, response: requests.Response):
        if apis.ResponseAxisCgi(response).is_textplain_response_with_error():
            raise AxisVapixExeption(response.text)

    def get_properties(self):
        kewargs = {
           RequestUrlParamType.GROUP.value: "root.Properties",
        }
        request = apis.RequestParameterManagement(self._host, self._port).get_request(ActionType.LIST, **kewargs)
        request.auth = self._session.auth
        response = self._session.send(request.prepare())
        self._ensure_response_status_ok(response)
        self._ensure_response_textplain(response)
        lines = response.text.strip().split("\n")
        for line in lines:
            key, value = line.split('=')
            if key == "root.Properties.System.SerialNumber":
                self._serial_number = value
            if key == "root.Properties.Firmware.Version":
                self._firmware_version = value
            if key == "root.Properties.FirmwareManagement.Version":
                self._firmware_management_version = get_firmwareversion_type_from_string(value)
            if key == "root.Properties.BasicDeviceInfo.BasicDeviceInfo":
                self._is_basic_device_info_supported = value
        self._is_device_properties_info_avaliable = True


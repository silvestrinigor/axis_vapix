from .apis import RequestAxisVapix
from .types import ApiPathType
from requests import Request

class RequestFirmwareManagementApi(RequestAxisVapix):
    """
    Property: Properties.FirmwareManagemenrequest_body_class = AxisRequestBodyt.Version=1.3
    API Discovery: id=fwmgr
    Firmware: 7.40 and later
    """
    def __init__(self, host: str, port: int, api_version: str, context = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_FIRMWARE_MANAGEMENT
    
    def status(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def upgrade(self, file_path: str):        
        json_data = b"""\
        {
        "apiVersion": "1.0",
        "method": "upgrade"
        }\
        """
        firmware = open(file_path, 'rb').read()
        return Request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", files=((None, json_data),(None, firmware)))
        
    def commit(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def roolback(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def purge(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def factory_default(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def stop_auto(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def reboot(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

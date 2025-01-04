from requests import Request
from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType
from ..params import ApiVersion

class RequestFirmwareManagementApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
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

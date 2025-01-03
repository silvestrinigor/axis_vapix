from .apis import RequestAxisVapix
from .types import ApiPathType

class RequestNtpApi(RequestAxisVapix):
    """
    API Discovery: id=ntp
    Property: Properties.API.HTTP.Version=3
    Firmware: 9.10 and later
    """
    def __init__(self, host, port, api_version = None, context = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_NTP.value
        
    def get_ntp_info(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
        
    def set_ntp_client_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

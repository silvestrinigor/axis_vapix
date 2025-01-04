from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType
from ..params import ApiVersion

class RequestNtpApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_NTP.value
        
    def get_ntp_info(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
        
    def set_ntp_client_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")

    def get_supported_versions(self):
        return super()._get_supported_versions()

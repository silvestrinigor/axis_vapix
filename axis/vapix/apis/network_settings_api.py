from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType
from ..params import ApiVersion

class RequestNetworkSettingsApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_NETWORK_SETTINGS_API
    
    def add_vlan(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def get_network_info(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def remove_vlam(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def scan_wlan_networks(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_hostname_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_ipv4_address_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_ipv6_address_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_global_proxy_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_resolver_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_wired_8021x_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_wlan_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def set_wlan_station_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def test_wlan_station_configuration(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")
    
    def wlan_switch_apto_station(self): # TODO: Implement this function
        raise NotImplementedError("This function is not implemented yet.")


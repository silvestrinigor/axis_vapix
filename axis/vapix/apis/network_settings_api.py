""""
https://developer.axis.com/vapix/network-video/network-settings-api
"""

from ..interfaces import IRequestAxisVapix
from ..types import ApiPathType, RequestParamType, MethodType
from ..params import ApiVersion, IPv4AddressConfiguration, FirmwareVersion

NETWORK_SETTINGS_API_LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 5, 0)
NETWORK_SETTINGS_API_DISCOVERY_API_ID = "network-settings"

class RequestNetworkSettingsApi(IRequestAxisVapix):

    def __init__(self, host: str, port: int, api_version: ApiVersion, context: str | None = None):
        super().__init__(host, port, api_version, context)
        self._api_path_type = ApiPathType.AXIS_CGI_NETWORK_SETTINGS_API
    
    def add_vlan(self, master_device_name: str, vlan_id: int):
        params = {
            "masterDeviceName": master_device_name,
            "VlanId": vlan_id
        }
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.PARAMS.value] = params
        request_body[RequestParamType.METHOD.value] = MethodType.ADD_VLAM.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def get_network_info(self): 
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.METHOD.value] = MethodType.GET_NETWORK_INFO.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def remove_vlam(self, master_device_name: str | None = None, vlan_id: int | None = None):
        params = {}
        if master_device_name is not None:
            params["masterDeviceName"] = master_device_name
        if vlan_id is not None:
            params["VlanId"] = vlan_id
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.PARAMS.value] = params
        request_body[RequestParamType.METHOD.value] = MethodType.REMOVE_VLAM.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def scan_wlan_networks(self, device_name: str, refresh: bool | None = None):
        params = {}
        params["masterDeviceName"] = device_name
        if refresh is not None:
            params["VlanId"] = refresh
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.PARAMS.value] = params
        request_body[RequestParamType.METHOD.value] = MethodType.SCAN_WLAN_NETWORKS.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_hostname_configuration(self, use_dhcp_hostname: bool | None = None, static_hostname: str | None = None):
        params = {}
        if use_dhcp_hostname is not None:
            params["useDhcpHostname"] = use_dhcp_hostname
        if static_hostname is not None:
            params["staticHostname"] = static_hostname
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.PARAMS.value] = params
        request_body[RequestParamType.METHOD.value] = MethodType.SET_HOSTNAME_CONFIGURATION.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

    def set_ipv4_address_configuration(self, ipv4_configuration: IPv4AddressConfiguration):
        request_body = self._get_basic_request_body()
        request_body[RequestParamType.PARAMS.value] = ipv4_configuration.get_all_params()
        request_body[RequestParamType.METHOD.value] = MethodType.SET_IPV4_ADDRESS_CONFIGURATION.value
        return self._create_request("POST", f"http://{self._host}:{self._port}/{self._api_path_type.value}", json= request_body)

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

    def get_supported_versions(self):
        return super()._get_supported_versions()
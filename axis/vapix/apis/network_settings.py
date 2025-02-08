"""
https://developer.axis.com/vapix/network-video/network-settings-api
"""

from enum import Enum
from dataclasses import dataclass, asdict
from ..connection import ApiVersion, FirmwareVersion
from ..interfaces import IVapixApi
from ..requests import AxisSession

PATH = "axis-cgi/network_settings.cgi"
LOWER_FIRMWARE_VERSION_SUPPORTED = FirmwareVersion(8, 50, 0)
DISCOVERY_API_ID = "network-settings"
REQUEST_METHOD = "POST"


PROPERTIES = [
    "Properties.API.HTTP.Version=3"
]


BODY = {
    "apiVersion": None,
    "context": None,
    "method": None,
    "params": None
}

class MethodType(Enum):
    ADD_VLAM = "addVlan"
    GET_NETWORK_INFO = "getNetworkInfo"
    GET_SUPPORTED_VERSIONS = "getSupportedVersions"
    REMOVE_VLAM = "removeVlan"
    SCAN_WLAN_NETWORKS = "scanWLANNetworks"
    SET_HOSTNAME_CONFIGURATION = "setHostnameConfiguration"
    SET_IPV4_ADDRESS_CONFIGURATION = "setIPv4AddressConfiguration"
    SET_IPV6_ADDRESS_CONFIGURATION = "setIPv6AddressConfiguration"
    SET_GLOBAL_PROXY_CONFIGURATION = "setGlobalProxyConfiguration"
    SET_RESOLVER_CONFIGURATION = "setResolverConfiguration"
    SET_WIRED_8021X_CONFIGURATION = "setWired8021XConfiguration"
    SET_WLAN_CONFIGURATION = "setWlanConfiguration"
    SET_WLAN_STATION_CONFIGURATION = "setWlanStationConfiguration"
    TEST_WLAN_STATION_SETTINGS = "setWlanStationSettings"
    WLAN_SWITCH_APTO_STATION = "wlanSwitchAPToStation"


class LinkLocalModeType(Enum):
    OFF = "off"
    ON = "on"
    FALLBACK = "fallback"


class IPAddressConfigurationModeType(Enum):
    DHCP = "DHCP"
    STATIC = "static"
    NONE = None
    
    
@dataclass
class HostnameConfiguration:
    useDhcpHostname: bool | None = None
    staticHostname: str | None = None


@dataclass
class StaticAddressConfigurations:
    address: str | None = None
    prefixLength: int | None = None
    broadcast: str | None = None


@dataclass  
class IPv4AddressConfiguration:
    deviceName: str | None = "eth0"
    enable: bool | None = None
    configurationMode: IPAddressConfigurationModeType = IPAddressConfigurationModeType.NONE
    linkLocalMode: LinkLocalModeType | None = None
    staticAddressConfigurations: list[StaticAddressConfigurations] = None
    useStaticDhcpFallback: bool | None = None
    useDhcpStaticRoutes: bool | None = None


class NetworkSettingsApi(IVapixApi):
    def __init__(self, session: AxisSession, api_version: ApiVersion):
        super().__init__(session, api_version, path=PATH)
    
    def add_vlan(self, master_device_name: str, vlan_id: int):
        params = {
            "masterDeviceName": master_device_name,
            "VlanId": vlan_id
        }
        body = self._create_body(MethodType.ADD_VLAM, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def get_network_info(self):
        body = self._create_body(MethodType.GET_NETWORK_INFO)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

    def remove_vlam(self, master_device_name: str | None = None, vlan_id: int | None = None):
        params = {}
        if master_device_name is not None:
            params["masterDeviceName"] = master_device_name
        if vlan_id is not None:
            params["VlanId"] = vlan_id
            
        body = self._create_body(MethodType.REMOVE_VLAM, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def scan_wlan_networks(self, device_name: str, refresh: bool | None = None):
        params = {}
        params["masterDeviceName"] = device_name
        if refresh is not None:
            params["VlanId"] = refresh
        
        body = self._create_body(MethodType.SCAN_WLAN_NETWORKS, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_hostname_configuration(self, use_dhcp_hostname: bool | None = None, static_hostname: str | None = None):
        params = {}
        if use_dhcp_hostname is not None:
            params["useDhcpHostname"] = use_dhcp_hostname
        if static_hostname is not None:
            params["staticHostname"] = static_hostname

        body = self._create_body(MethodType.SET_HOSTNAME_CONFIGURATION, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response
    
    def set_ipv4_address_configuration(self, configuration: IPv4AddressConfiguration):
        params = asdict(configuration)
        body = self._create_body(MethodType.SET_IPV4_ADDRESS_CONFIGURATION, params)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response

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
        body = self._create_body(MethodType.GET_SUPPORTED_VERSIONS)
        request = self._create_request(body, REQUEST_METHOD)
        response = self._send_request(request)
        return response